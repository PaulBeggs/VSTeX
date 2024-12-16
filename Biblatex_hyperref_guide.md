GitHub Copilot: Certainly! Both the `biblatex` and `hyperref` packages in LaTeX work together to manage and enhance citations in your documents. Below is a comprehensive overview of the citation commands provided by `biblatex`, along with how `hyperref` integrates with them to produce hyperlinked references.

## **1. Interaction Between `biblatex` and `hyperref`**

- **`biblatex`**: A powerful and flexible package for handling bibliographies and citations. It offers a wide range of commands to customize how citations appear in your document.
  
- **`hyperref`**: Enhances your document by adding hyperlinks to references, citations, table of contents, and more. When used in conjunction with `biblatex`, it automatically converts citation references into clickable hyperlinks that navigate to the corresponding bibliography entries.

**Note**: Ensure that you load `hyperref` **after** `biblatex` in your preamble to allow proper integration.

```latex
\usepackage[style=apa,backend=biber]{biblatex}
\usepackage{hyperref}
```

## **2. Common `biblatex` Citation Commands**

Below is a categorized list of `biblatex` citation commands. Each command is accompanied by a brief description and an example of its usage.

### **A. General Citation Commands**

1. **`\cite{key}`**
   - **Description**: The most basic citation command. Its output format depends on the citation style and context.
   - **Example**: 
     ```latex
     According to \cite{smith2020study}, ...
     ```

2. **`\parencite{key}`**
   - **Description**: Produces a parenthetical citation, typically formatted as `(Author, Year)`.
   - **Example**:
     ```latex
     This theory has been supported by recent studies \parencite{doe2019research}.
     ```

3. **`\textcite{key}`**
   - **Description**: Integrates the citation into the text, usually formatted as `Author (Year)`.
   - **Example**:
     ```latex
     \textcite{johnson2021analysis} argues that ...
     ```

4. **`\footcite{key}`**
   - **Description**: Places the citation in a footnote.
   - **Example**:
     ```latex
     This phenomenon is well-documented.\footcite{lee2018overview}
     ```

5. **`\supercite{key}`**
   - **Description**: Creates a superscripted citation, common in some journals.
   - **Example**:
     ```latex
     The results were inconclusive.\supercite{kim2022study}
     ```

6. **`\autocite{key}`**
   - **Description**: Automatically selects between `\parencite` or `\footcite` based on the configured citation mode.
   - **Example**:
     ```latex
     Previous research supports this claim \autocite{williams2020findings}.
     ```

7. **`\smartcite{key}`**
   - **Description**: Switches between `\textcite` and `\parencite` intelligently, adapting to the sentence structure.
   - **Example**:
     ```latex
     \smartcite{brown2017theory} provides an alternative perspective.
     ```

### **B. Full Citation Commands**

1. **`\fullcite{key}`**
   - **Description**: Produces a full citation as it would appear in the bibliography.
   - **Example**:
     ```latex
     For a comprehensive review, see \fullcite{miller2016comprehensive}.
     ```

2. **`\citeauthor{key}`**
   - **Description**: Cites only the author(s) of the work.
   - **Example**:
     ```latex
     According to \citeauthor{davis2015approach}, ...
     ```

3. **`\citetitle{key}`**
   - **Description**: Cites only the title of the work.
   - **Example**:
     ```latex
     The study titled "\citetitle{thompson2019insights}" explores...
     ```

4. **`\citeyear{key}`**
   - **Description**: Cites only the year of publication.
   - **Example**:
     ```latex
     The theory was first introduced in \citeyear{garcia2014foundations}.
     ```

### **C. Extended Citation Commands**

1. **`\citealt{key}`**
   - **Description**: Acts like `\cite`, but without any enclosing parentheses.
   - **Example**:
     ```latex
     \citealt{evans2021study} found that...
     ```

2. **`\citealp{key}`**
   - **Description**: Similar to `\citealt`, producing a citation without parentheses and without a preceding space.
   - **Example**:
     ```latex
     Many researchers \citealp{martin2018analysis} agree...
     ```

3. **`\cites{key1}{key2}{key3}`**
   - **Description**: Cites multiple sources in a single command.
   - **Example**:
     ```latex
     Several studies have addressed this issue \cites{lee2017,kim2018,park2019}.
     ```

4. **`\citeauthor*{key}`**
   - **Description**: Cites all authors without abbreviation.
   - **Example**:
     ```latex
     \citeauthor*{white2020comprehensive} discuss...
     ```

### **D. Specialized Citation Commands**

1. **`\nocite{key}`**
   - **Description**: Includes the citation in the bibliography without citing it in the text.
   - **Example**:
     ```latex
     \nocite{allen2016development}
     ```

2. **`\footcitetext{...}`**
   - **Description**: Inserts arbitrary text as a footnote, not necessarily linked to a citation.
   - **Example**:
     ```latex
     This concept is widely accepted.\footcitetext{Further details can be found in the supplementary materials.}
     ```

3. **`\DeclareCiteCommand`**
   - **Description**: Allows customization of how citations are formatted.
   - **Usage**: Advanced users defining custom citation styles.

4. **`\mkbibnamegiven` and `\mkbibnamefamily`**
   - **Description**: Formats the given and family names in citations.
   - **Usage**: Customizing name formats in citations.

### **E. Citation Commands with Pre/Post Notes**

1. **`\cite[pre][post]{key}`**
   - **Description**: Adds text before and/or after the citation.
   - **Example**:
     ```latex
     \cite[see][for details]{thompson2019insights}
     ```
     - **Output**: (see Author, Year for details)

2. **`\parencite[pre][post]{key}`**
   - **Description**: Similar to `\parencite` but with pre and post notes.
   - **Example**:
     ```latex
     \parencite[discussed in][p. 15]{johnson2020theory}
     ```
     - **Output**: (discussed in Author, Year, p. 15)

3. **`\textcite[pre][post]{key}`**
   - **Description**: Similar to `\textcite` but with pre and post notes.
   - **Example**:
     ```latex
     \textcite{smith2018research}[argues that]
     ```
     - **Output**: Author (Year) argues that...

## **3. Advanced `biblatex` Citation Features**

### **A. Citation Styles and Aliases**

- **`\autocite` and `\smartcite`**: These commands offer more flexibility in citation styles by adapting to different contexts or user-defined preferences.

### **B. Citation Chains**

- **`\citerangeto{key1}{key2}`**: Cites a range of entries from `key1` to `key2`.
  - **Example**:
    ```latex
    \citerangeto{smith2018}{johnson2020}
    ```

### **C. Localization and Language Support**

- `biblatex` supports multiple languages, allowing citation commands to adapt to different language conventions.

### **D. Custom Citation Commands**

- Users can define their own citation commands using `\DeclareCiteCommand`, enabling highly customized citation outputs tailored to specific needs.

## **4. Recommendations and Best Practices**

1. **Consistent Citation Style**:
   - Ensure that your citation commands align with the chosen bibliography style (`apa` in your case).
  
2. **Using `\parencite` and `\textcite`**:
   - Prefer using `\parencite` for parenthetical citations and `\textcite` for in-text citations to maintain clarity and readability.

3. **Managing Multiple Citations**:
   - Use `\cites` or separate commands to handle multiple references efficiently.

4. **Customizing Citations**:
   - Leverage the flexibility of `biblatex` to define custom citation formats if necessary, especially when adhering to specific publication guidelines.

5. **Consult Documentation**:
   - For exhaustive details and advanced features, refer to the [biblatex documentation](https://mirrors.ctan.org/macros/latex/contrib/biblatex/doc/biblatex.pdf) and the [hyperref documentation](https://ctan.org/pkg/hyperref).

## **5. Example Usage in Your Document**

Here's how you might incorporate some of these citation commands into your LaTeX document:

```latex
\documentclass[stu]{apa7}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{enumitem}
\usepackage{geometry}
\linespread{1}
\usepackage[style=apa,backend=biber]{biblatex}
\usepackage{hyperref}
\usepackage{xcolor}
\definecolor{horange}{HTML}{f58026}
\hypersetup{
	colorlinks=true,
	linkcolor=horange,
	filecolor=horange,      
	urlcolor=horange,
    citecolor=horange
}
\usepackage{C:/Users/paulb/VSTeX/local/draculatheme}
\addbibresource{references.bib}

\title{Annotated Bibliography: The Effect of ADHD on Cognition}
\shorttitle{The Effect of ADHD on Cognition}
\author{Paul Beggs}
\authorsaffiliations{Hendrix College}
\course{PSYC 319: Cognitive Psychology}
\professor{Dr.\ Carmen Merrick}
\duedate{November 14, 2024}

\abstract{
	TODO: Write abstract.
}

\begin{document}

\maketitle

\section{Introduction}

In exploring the impact of ADHD on cognitive functions, recent studies have highlighted significant correlations between attention deficits and problem-solving abilities \parencite{drigas_executive_2019}. Moreover, understanding how individuals with ADHD navigate cognitive challenges can provide deeper insights into empathetic development \textcite{faraone_attention-deficithyperactivity_2015}.

\printbibliography

\end{document}
```

**Explanation**:

- **`\parencite{drigas_executive_2019}`**: Inserts a parenthetical citation like `(Drigas & Karyotaki, 2019)`.
  
- **`\textcite{faraone_attention-deficithyperactivity_2015}`**: Inserts an in-text citation like `Faraone et al. (2015)`.

## **6. Troubleshooting Common Issues**

1. **Missing Bibliography Entries**:
   - Ensure that all cited keys (e.g., `drigas_executive_2019`) are present in your `references.bib` file.
  
2. **Inconsistent Citation Output**:
   - Verify that the selected citation commands align with your bibliography style (`apa`).
  
3. **Hyperlinks Not Working**:
   - Make sure `hyperref` is loaded **after** `biblatex`.
   - Compile your document using `pdflatex` followed by `biber` and then `pdflatex` twice to ensure proper hyperlink creation.

4. **Compilation Errors**:
   - Check for syntax errors in both your `.tex` and `.bib` files.
   - Ensure that all required packages are installed and updated.

## **7. Additional Resources**

- **`biblatex` Package Documentation**: [CTAN - biblatex](https://ctan.org/pkg/biblatex)
- **`hyperref` Package Documentation**: [CTAN - hyperref](https://ctan.org/pkg/hyperref)
- **Comprehensive `biblatex` Tutorial**: [Overleaf - biblatex](https://www.overleaf.com/learn/latex/Bibliography_management_with_biblatex_and_biber)

---

By utilizing these `biblatex` citation commands in conjunction with `hyperref`, you can create a robust and well-formatted bibliography with clickable, hyperlinked references that enhance the navigability and professionalism of your LaTeX documents.