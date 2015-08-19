"""A script to invoke the builder and build theme files.
"""

import builder

builder.generate_color_scheme_from_files(
    "Rainbow (Light)",
        "common.theme-definition", "light.theme-definition"
)
builder.generate_color_scheme_from_files(
    "Rainbow (Dark)",
        "common.theme-definition", "dark.theme-definition"
)
