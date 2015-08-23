function update_preview(object, background, foreground) {
    object.css("background", background.toHexString()).css("color", foreground.toHexString());
}

function update_information(object, background, foreground, threshold) {
    var contrast_ratio = tinycolor.readability(background, foreground);
    var is_readable = contrast_ratio > threshold;

    object.find(".contrast-ratio").text(contrast_ratio);
    object.find(".is-readable").text(is_readable);
}

function update_color_suggestions(foreground, dark_color, light_color, range, gap, threshold, suggestions_check_light, suggestions_check_dark) {
    function clamp(value, min, max) {
        if (value < min) {
            return min;
        } else if (value > max) {
            return max;
        } else {
            return value;
        }
    }

    // Determine the range of colours we check
    var hsv = foreground.toHsv();
    var min_v, max_v,
        min_s, max_s;

    min_v = clamp(hsv.v - range, 0, 1);
    max_v = clamp(hsv.v + range, 0, 1);

    min_s = clamp(hsv.s - range, 0, 1);
    if (hsv.s == 0) {
        max_s = 0;
    } else {
        max_s = clamp(hsv.s + range, 0, 1);
    }

    var color, light_contrast, dark_contrast, foreground_colors;

    var h = hsv.h, suggestions = [];
    for (var v = min_v; v <= max_v; v += gap) {
        for (var s = min_s; s <= max_s; s += gap) {
            // Check if color passes filters...
            color = tinycolor({h: h, s: s, v: v})
            light_contrast = tinycolor.readability(light_color, color);
            dark_contrast = tinycolor.readability(dark_color, color);
            if (light_contrast < threshold && suggestions_check_light) {
                continue;
            }
            if (dark_contrast < threshold && suggestions_check_dark) {
                continue;
            }

            if (hsv.s == 0) {
                foreground_colors = [
                    {h: hsv.h, v: 90, s: s},
                    {h: hsv.h, v: 10, s: s}
                ];
            } else {
                foreground_colors = [
                    {h: hsv.h, v: 75, s: s},
                    {h: hsv.h, v: 25, s: s}
                ];
            }
            // Add object
            suggestions.push({
                color: color,
                fore_hex: tinycolor.mostReadable(color, foreground_colors, {includeFallbackColors: false}).toHexString(),
                light_contrast: light_contrast,
                dark_contrast: dark_contrast
            });
        };
    }
    if (!suggestions_check_light && !suggestions_check_dark) {
        $("#color-suggestions").text("Select at least one 'Check Contrast with ...' option to get suggestions.");
    } else if (suggestions.length == 0) {
        $("#color-suggestions").text("No suggestions found. Try changing the range and/or gap.");
    } else {
        // Comparator
        var key;
        if (suggestions_check_light && suggestions_check_dark) {
            var key = function key(a, b) {
                var f = function (x) {
                    return (
                        Math.max(x.light_contrast, x.dark_contrast) /
                        Math.min(x.light_contrast, x.dark_contrast)
                    );
                };
                return f(a) - f(b);
            };
        } else if (suggestions_check_dark) {
            var key = function dark_key(a, b) {
                return Math.abs(a.dark_contrast - b.dark_contrast);
            };
        } else if (suggestions_check_light) {
            var key = function light_key(a, b) {
                return Math.abs(a.light_contrast - b.light_contrast);
            }
        } else {
            console.error("Should not have reached here!!");
            return;
        }
        suggestions.sort(key);

        var parts = [], obj;

        for (var i = 0; i < suggestions.length; i++) {
            obj = suggestions[i];
            parts.push(`
                <div class="color-box col-xs-4 col-sm-3 col-md-2 text-center"
                     style="background: ${obj.color.toHexString()}; color: ${obj.fore_hex};"
                >
                    <span class="color-hsv">
                        ${obj.color.toHsvString()}
                    </span>
                    <span class="color-hex">
                        ${obj.color.toHexString().toUpperCase()}
                    </span>
                    <span class="color-contrast-light">
                        ${obj.light_contrast.toFixed(3)}
                    </span>
                    <span class="color-contrast-dark">
                        ${obj.dark_contrast.toFixed(3)}
                    </span>
                </div>
            `);
        }
        $("#color-suggestions").html(parts.join(""));
    }
    $(".color-hex").click(function on_color_hex_click() {
        var hex_val = $(this).text().trim();
        $("#color-foreground-input").val(hex_val).change();
    });
}

function on_color_change(event) {
    // Get the input
    var foreground = tinycolor($("#color-foreground-input").val());
    var dark_color = tinycolor($("#color-dark-input").val());
    var light_color = tinycolor($("#color-light-input").val());

    var range = parseFloat($("#suggestions-range").val());
    var gap = parseFloat($("#suggestions-gap").val());
    var threshold = parseFloat($("#suggestions-threshold").val());

    var suggestions_check_light = $("#suggestions-check-light").is(":checked");
    var suggestions_check_dark = $("#suggestions-check-dark").is(":checked");

    if (gap == 0) {
        gap = 1;
    }

    // Previews
    var preview_box_light = $("#preview-box-light");
    var preview_box_dark = $("#preview-box-dark");

    update_preview(preview_box_light, light_color, foreground);
    update_preview(preview_box_dark, dark_color, foreground);

    // Information
    var information_box_light = $("#information-box-light");
    var information_box_dark = $("#information-box-dark");

    update_information(information_box_light, light_color, foreground, threshold);
    update_information(information_box_dark, dark_color, foreground, threshold);

    // Color Addons
    $("#input-addon-dark").text(dark_color.toHexString().toUpperCase());
    $("#input-addon-light").text(light_color.toHexString().toUpperCase());
    $("#input-addon-foreground").text(foreground.toHexString().toUpperCase());

    update_color_suggestions(foreground, dark_color, light_color, range, gap, threshold, suggestions_check_light, suggestions_check_dark);
}

$(function() {
    on_color_change();

    $(".form-control").change(on_color_change);
});
