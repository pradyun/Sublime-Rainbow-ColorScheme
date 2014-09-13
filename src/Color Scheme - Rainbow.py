#!/usr/bin/python
"""Rainbow color scheme generation
"""
import builder
from builder import transparency, grey, blend, shade, saturate

# Rainbow colors, base of scheme
red = "#FF0000"
violet = "#AA80FF"
blue = "#0000FF"
green = "#00FF00"
yellow = "#FFCC00"
orange = "#ED5F21"

# Other colors
white = grey(100)
black = grey(0)

gold = "#FFD700"
pink = "#EE00AA"
purple = "#EE82EE"
blue2 = "#007AC3"

dark_red = "#CC3333"
light_blue = "#66CCFF"
dark_blue = "#000066"
dark_green = "#009400"

background = blend(grey(95), blue, 4)
# foreground = grey(15)
foreground = blend(grey(15), blue, 10)

scheme = {
    "name": "Rainbow",
    "uuid": "0E945910-0FE8-47DF-8EFF-F63DDDB860C6",
    "settings": [
        {  # General
            "name": "General",
            "settings": {
                "background": background,
                "foreground": foreground,
                "gutter": transparency(black, 10),

                "caret": grey(15),
                "lineHighlight": transparency(foreground, 3),

                "selection": blend(foreground, background, 95),
                "selectionBorder": grey(70),

                "findHighlight": blend(yellow, background),
                "findHighlightBorder": grey(70),
                "findHighlightForeground": grey(0),

                "bracketsForeground": grey(60),
                "bracketsOptions": "underline",

                # "tagsOptions": "stippled_underline",

                "guide": grey(80),
                "activeGuide": grey(65),

                "invisibles": foreground
            }
        },
        # Whitespace highlighting
        {
            "name": "Trailing WhiteSpace",
            "scope": "whitespace.trailing",
            "settings": {
                "background": blend(red, background, 97)
            }
        }
    ]
}

#------------------------------------------------------------------------------
# Python
#------------------------------------------------------------------------------
scheme["settings"] += [
    {  # Comment
        "name": "Comment",
        "scope": "comment, punctuation.definition.comment",
        "settings": {
            "foreground": grey(60),
        }
    },
    {  # Comment notes
        "name": "Note Comment",
        "scope": "comment.line.note.notation",
        "settings": {
            "foreground": blend(red, grey(60), 60),
        }
    },
    {  # String
        "name": "String",
        "scope": "string",
        "settings": {
            "foreground": dark_green,
        }
    },
    {  # Keywords
        "name": "Keyword",
        "scope": "keyword",
        "settings": {
            "foreground": orange,
        }
    },
    # { # Operator
    #     "name": "Operator",
    #     "scope": "keyword.operator",
    #     "settings": {
    #         "foreground": transparency(purple, 65),
    #     }
    # },
    {  # Variable
        "name": "Variable",
        "scope": "variable",
        "settings": {
            "foreground": blend(dark_blue, grey(50))
        }
    },
    {  # Parameter
        "name": "Parameter",
        "scope": "variable.parameter",
        "settings": {
            "foreground": shade(blend(green, blue), 10)
        }
    },
    {  # Constant
        "name": "Constants",
        "scope": "constant",
        "settings": {
            "foreground": shade(saturate(purple, 20), -30)
        }
    },
    # {
    #     "name": "Built-in constant",
    #     "scope": "constant.language",
    #     "settings": {
    #         "foreground": shade(purple, 20)
    #     }
    # },
    {  # Number
        "name": "Number",
        "scope": "constant.numeric",
        "settings": {
            "foreground": shade(blend(blue, dark_red, 70), 20)
        }
    },
    {  # Character Constant
        "name": "Character constant",
        "scope": "constant.character",
        "settings": {
            "foreground": saturate(blend(purple, green, 10), 30)
        }
    },
    {  # Storage (class, def etc)
        "name": "Storage",
        "scope": "storage",
        "settings": {
            "foreground": dark_red,
        }
    },
    {  # Support: Function
        "name": "Support function",
        "scope": "support.function",
        "settings": {
            "foreground": blend(light_blue, dark_blue)
        }
    },
    {  # Support: Class/Type
        "name": "Support class or type",
        "scope": "support.type, support.class",
        "settings": {
            "foreground": blend(green, blue, 35)
        }
    },
    # {
    #     "name": "Storage type",
    #     "scope": "storage.type",
    #     "settings": {
    #         "foreground": shade(blue, -30)
    #     }
    # },
    # {
    #     "name": "Support constant",
    #     "scope": "support.constant",
    #     "settings": {
    #         "foreground": "#66D9EF",
    #         "fontStyle": ""
    #     }
    # },
    # {
    #     "name": "Support variable",
    #     "scope": "support.other.variable",
    #     "settings": {
    #         "fontStyle": ""
    #     }
    # },
    {  # Class name
        "name": "Class name",
        "scope": "entity.name.class, entity.name.type.class",
        "settings": {
            "foreground": transparency(dark_blue, 80)
        }
    },
    {  # Class inherited from
        "name": "Inherited class",
        "scope": "entity.other.inherited-class",
        "settings": {
            "foreground": shade(yellow, -20)
        }
    },
    {  # Function name
        "name": "Function name",
        "scope": "entity.name.function",
        "settings": {
            "foreground": blend(dark_blue, blue2, 80)
        }
    },
    {  # Decorator
        "name": "Decorator",
        "scope": "entity.name.function.decorator",
        "settings": {
            "foreground": blend(dark_red, green, 35)
        }
    },
    {  # Invalid
        "scope": "invalid",
        "name": "Invalid",
        "settings": {
            "fontStyle": "",
            "foreground": blend(red, foreground, 30),
            "background": blend(red, background)
        }
    },
    {  # Deprecated
        "scope": "invalid.deprecated",
        "name": "Deprecated stuff",
        "settings": {
            "background": "#F82820",
        }
    }
]

#------------------------------------------------------------------------------
# General
#------------------------------------------------------------------------------
scheme["settings"] += [
    {  # Entity name
        "name": "Entity name",
        "scope": "entity.name",
        "settings": {
            "foreground": blend(dark_blue, blue2, 80)
        }
    },
]

#------------------------------------------------------------------------------
# HTML/XML
#------------------------------------------------------------------------------
scheme["settings"] += [
    {  # Tag attribute name
        "name": "Tags",
        "scope": "entity.other.attribute-name",
        "settings": {
            "foreground": orange
        }
    },
    {  # Tag name
        "name": "Tags",
        "scope": "entity.name.tag",
        "settings": {
            "foreground": dark_red
        }
    }
]
#------------------------------------------------------------------------------
# Git Gutter/Diff
#------------------------------------------------------------------------------
scheme["settings"] += [
    {  # Deleted
        "scope": "markup.deleted",
        "name": "Git deleted",
        "settings": {
            "foreground": dark_red
        }
    },
    {  # Inserted
        "scope": "markup.inserted",
        "name": "Git inserted",
        "settings": {
            "foreground": dark_green
        }
    },
    {  # Changed
        "scope": "markup.changed",
        "name": "Git changed",
        "settings": {
            "foreground": dark_green
        }
    },
    {  # Ignored
        "scope": "markup.ignored",
        "name": "Git ignored",
        "settings": {
            "foreground": grey(50)
        }
    },
    {  # Untracked
        "scope": "markup.untracked",
        "name": "Git untracked",
        "settings": {
            "foreground": grey(50)
        }
    },
    {  # Diff: Context lines
        "scope": "source.diff",
        "name": "Git Diff",
        "settings": {
            "foreground": grey(30)
        }
    },
    {  # Diff: Headers
        "scope": "meta.diff.header",
        "name": "Git diff file header",
        "settings": {
            "foreground": black
        }
    }
]

#------------------------------------------------------------------------------
# Pylinter
#------------------------------------------------------------------------------
scheme["settings"] += [
    # All things are trasparent slightly. But they have their own colors. So,
    # using white as the Foreground mean all the colors as they are by default.
    {
        "scope": "pylinter",
        "settings": {
            "foreground": white
        }
    }
]

#------------------------------------------------------------------------------
# Markdown
#------------------------------------------------------------------------------
scheme["settings"] += [
    {  # Inline Raw
        "name": "Markup: raw inline",
        "scope": "text.html.markdown markup.raw.inline",
        "settings": {
            "foreground": blend(violet, foreground)
        }
    },
    {  # Linebreak
        "name": "Markdown: linebreak",
        "scope": "text.html.markdown meta.dummy.line-break",
        "settings": {
            "background": transparency(violet, 80)
        }
    },
    {  # Heading
        "name": "Markdown: heading",
        "scope": "markdown.heading, markup.heading | markup.heading entity.name, markup.heading.markdown punctuation.definition.heading.markdown",
        "settings": {
            "foreground": orange
        }
    },
    {  # Italic
        "name": "Markup: italic",
        "scope": "markup.italic",
        "settings": {
            "fontStyle": "italic",
            "foreground": dark_red
        }
    },
    {  # Bold
        "name": "Markup: bold",
        "scope": "markup.bold",
        "settings": {
            "fontStyle": "bold",
            "foreground": blend(dark_red, foreground, 30)
        }
    },
    {  # Underline
        "name": "Markup: underline",
        "scope": "markup.underline",
        "settings": {
            "fontStyle": "underline",
            "foreground": blend(dark_red, foreground, 15)
        }
    },
    {  # Blockquote
        "name": "Markdown: Blockquote",
        "scope": "markup.quote, punctuation.definition.blockquote.markdown",
        "settings": {
            "foreground": blue
        }
    },
    {  # Quote
        "name": "Markup: Quote",
        "scope": "markup.quote",
        "settings": {
            "foreground": blend(blue, foreground)
        }
    },
    {  # Links
        "name": "Markdown: Link",
        "scope": "string.other.link.title.markdown",
        "settings": {
            "fontStyle": "underline",
            "foreground": blend(green, foreground)
        }
    },
    {  # Block Raw
        "name": "Markup: Raw block",
        "scope": "markup.raw.block",
        "settings": {
            "foreground": blend(violet, foreground)
        }
    },
    {  # List items
        "name": "Markdown: List Items Punctuation",
        "scope": "punctuation.definition.list_item.markdown",
        "settings": {
            # "foreground": "#ffffff"
        }
    },
    {  # Fenced Block Raw
        "name": "Markdown: Raw Block fenced",
        "scope": "markup.raw.block.fenced.markdown",
        "settings": {
            "background": blend(black, background, 97)
        }
    },
    {  # Fenced Code Block
        "name": "Markdown: Fenced Code Block",
        "scope": "punctuation.definition.fenced.markdown, variable.language.fenced.markdown",
        "settings": {
            "background": blend(black, background, 97),
            "foreground": blue
            # "foreground": "#636050"
        }
    },
    {  # Fenced Language
        "name": "Markdown: Fenced Language",
        "scope": "variable.language.fenced.markdown",
        "settings": {
            "fontStyle": "",
            "foreground": violet
        }
    },
    {  # Markdown Seperator
        "name": "Markdown: Separator",
        "scope": "meta.separator",
        "settings": {
            "background": transparency(black, 5),
            "fontStyle": "bold"
        }
    },
]

#------------------------------------------------------------------------------
# Bracket Highlighter
#------------------------------------------------------------------------------
scheme["settings"] += [
    {  # Default (Used when the bracket does not have it's own scope)
        "name": "BracketHighlighter: Default",
        "scope": "bracket.default",
        "settings": {
            "fontStyle": "underline",
            "foreground": transparency(orange, 70)
        }
    },
    {  # String Quotes
        "name": "BracketHighlighter: Strings",
        "scope": "bracket.string",
        "settings": {
            "fontStyle": "underline",
            "foreground": transparency(dark_green, 80)
        }
    },
    {  # Curly
        "name": "BracketHighlighter: Curly",
        "scope": "bracket.curly",
        "settings": {
            "fontStyle": "",
            "foreground": transparency(orange, 70)
        }
    },
    {  # Square
        "name": "BracketHighlighter: Square",
        "scope": "bracket.square",
        "settings": {
            "fontStyle": "",
            "foreground": transparency(blue, 60)
        }
    },
    {  # Round
        "name": "BracketHighlighter: Round",
        "scope": "bracket.round",
        "settings": {
            "fontStyle": "",
            "foreground": blend(foreground, violet, 75)
        }
    },
    {  # Angle
        "name": "BracketHighlighter: Angle",
        "scope": "bracket.angle",
        "settings": {
            "fontStyle": "",
            "foreground": transparency(red, 50)
        }
    },
    {  # Tags
        "name": "BracketHighlighter: Tags",
        "scope": "bracket.tag",
        "settings": {
            "fontStyle": "",
            "foreground": dark_red
        }
    }
]

#------------------------------------------------------------------------------
# Building the scheme
#------------------------------------------------------------------------------
if __name__ == '__main__':
    builder.generate_color_scheme("Rainbow", scheme)
