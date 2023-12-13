\ProvidesClass{BusMateSRS}
\LoadClass[12pt,a4paper,numbers=enddot]{scrreprt}
\usepackage{geometry} % automate margins calculations
\usepackage{tabularx} % Enhanced tables
\usepackage{hyperref} % useful for PDF links
\hypersetup{hidelinks}
%% Config Fonts
\usepackage[sfdefault]{notomath} % Use Noto fonts for the whole document
%% Config Header and footer
\usepackage{fancyhdr}
\fancyhead[]{} % Clear header
\fancyfoot[]{} % Clear footer
\fancyfoot[l]{Software Requirements Specification for \emph{\projectName}}
\fancyfoot[r]{Page {\thepage}}
\renewcommand{\headrulewidth}{0pt}
\pagestyle{fancy}
\fancypagestyle{plain}{\pagestyle{fancy}\fancyhead[]{}}
%% Config Colors
\usepackage[dvipsnames]{xcolor}
\newcommand{\colorMain}{\color{Blue}}
\newcommand{\colorSecondary}{\color{RoyalBlue}}
%% Config Formatting Chapters
\usepackage{sectsty}
\renewcommand*{\chapterformat}{%
\mbox{\chapappifchapterprefix{\nobreakspace}\thechapter\autodot
\IfUsePrefixLine{}{\hspace{4cm}}}\;}
\chapterfont{\colorMain}
\chapterfont{\colorMain}
\sectionfont{\colorSecondary}
\subsectionfont{\colorSecondary}
%% Config title page
\title{\colorMain{\emph{\projectName}: \projectShortDescription}}
\subtitle{\colorSecondary{\docVersion}}
\author{\nameAndrew\\\nameKarim\\\nameHamdy\\\nameHossam}
\subject{Software Requirements Specification}
\publishers{\docPublishers}
