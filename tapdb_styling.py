# SELECT question, md(answer) FROM cards WHERE category = 'python'

# import html
# import sqlite3
import markdown

styling = """
    * { 
    font-family: 'gentium';
    font-size: 20px;
    white-space: pre;
    }

    /* not registered in sqlite */
    .front {text-align: center; font-size: 50pt;}
    .back {text-align: left;}
    .back_plus {text-align: left; margin-top: 30px}

    /* registered in sqlite */
    .deva {font-family: 'sanskrit 2003'; font-size: 80px;}
    .greek {font-family: 'new athena unicode'; font-size: 60px; text-align: center;}
    .cyr {font-family: 'monomakh unicode'; font-size: 60px;}
    .hanzi {font-family: 'tw-kai'; font-size: 100px;}
    .markdown{white-space: pre-wrap;}

    .markdown code, .markdown pre {
    font-family: monospace;
    }
    .markdown em {
    color: rgba(255, 255, 255, 153);
    }
"""

def wrap_style(text, css_class):
    return f'<div class="{css_class}">{text}</div>' if text else ""

def md(text, css_class):
    html =  markdown.markdown(text, extensions=['extra'])
    return f'<div class="{css_class}">{html}</div>' if text else ""
