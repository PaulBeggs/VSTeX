import os
import sys
import io
import ollama
from pdf2image import convert_from_path

# Configuration
# Note: Ensure you have pulled this model in Ollama (e.g., `ollama pull qwen2.5-vl`)
# If "qwen3-vl:2b" is a custom model or typo, adjust the string below.
MODEL_NAME = "qwen3-vl:2b" 

def convert_pdf_to_images(pdf_path):
    """
    Converts a PDF file into a list of byte streams (images).
    """
    print(f"Reading PDF from: {pdf_path}...")
    try:
        # Convert PDF pages to PIL images
        # fmt='jpeg' is usually lighter on token usage/memory than png
        pages = convert_from_path(pdf_path, fmt='jpeg')
        
        image_bytes_list = []
        
        print(f"Processing {len(pages)} pages...")
        
        for page in pages:
            # Resize large pages to avoid blowing up context window (optional but recommended)
            # Resizing to max dimension 1024 preserves detail while saving VRAM
            page.thumbnail((1024, 1024))
            
            # Convert PIL image to BytesIO
            img_byte_arr = io.BytesIO()
            page.save(img_byte_arr, format='JPEG')
            # Get binary data
            image_bytes_list.append(img_byte_arr.getvalue())
            
        return image_bytes_list
        
    except Exception as e:
        print(f"Error converting PDF: {e}")
        return None

def chat_loop(image_data):
    """
    Main loop for asking questions about the loaded images.
    """
    print("\n" + "="*50)
    print(f"PDF loaded! You are chatting with {MODEL_NAME}.")
    print("Type 'exit', 'quit', or 'q' to stop.")
    print("="*50 + "\n")

    # Initialize conversation history with a system prompt
    # This helps the model understand its role and reduces "one-word" failures.
    history = [
        {
            'role': 'system', 
            'content': 'You are a helpful assistant designed to analyze PDF documents. Use the provided images to answer the user\'s questions detailedly.'
        }
    ]

    # ANSI escape codes for coloring thinking process
    GREY_COLOR = "\033[90m"
    RESET_COLOR = "\033[0m"

    while True:
        try:
            user_input = input("Ask a question about the PDF: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("Goodbye!")
                break
            
            if not user_input:
                continue

            # Construct the user message
            user_message = {
                'role': 'user',
                'content': user_input,
            }

            # Only attach images to the first user query to save context window space.
            # The model will recall the images from the conversation history.
            if len(history) == 1:  # history only has system prompt
                user_message['images'] = image_data

            # Prepare messages list for this turn
            current_messages = history + [user_message]

            print("\n> ", end="", flush=True)

            # Call Ollama
            response = ollama.chat(
                model=MODEL_NAME,
                messages=current_messages,
                stream=True 
            )
            
            full_response = ""
            
            # Print streamed chunks
            for chunk in response:
                content = chunk['message']['content']
                
                # Check for thinking tags to apply color
                # Note: This is a simple check; if tags are split across chunks, 
                # color might apply slightly late, but it generally works well.
                if "<think>" in content:
                    print(GREY_COLOR, end="")
                
                print(content, end='', flush=True)
                full_response += content

                if "</think>" in content:
                    print(RESET_COLOR, end="")
            
            # Ensure color is reset at the end just in case
            print(RESET_COLOR + "\n")

            # Update history only after a successful turn
            history.append(user_message)
            history.append({'role': 'assistant', 'content': full_response})

        except KeyboardInterrupt:
            print(RESET_COLOR + "\nExiting...")
            break
        except Exception as e:
            print(RESET_COLOR + f"\nAn error occurred: {e}")

def main():
    print("--- PDF Analysis Tool with Ollama ---")
    
    while True:
        pdf_path = input("Please enter the full path to your PDF file: ").strip()
        
        # Remove quotes if user copied path as "C:\path\..."
        pdf_path = pdf_path.strip('"').strip("'")
        
        if os.path.exists(pdf_path) and pdf_path.lower().endswith('.pdf'):
            break
        else:
            print("Error: File not found or is not a PDF. Please try again.")

    # Convert PDF to images
    images = convert_pdf_to_images(pdf_path)
    
    if images:
        chat_loop(images)
    else:
        print("Failed to load PDF images.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated.")