#!/usr/bin/env bash

WALLPAPER_DIR="$HOME/Pictures/wallpapers/"
ALACRITTY_CONF="$HOME/.config/alacritty/alacritty.toml"
QTILE_CONF="$HOME/.config/qtile/config.py"
QTILE_AUTOSTART="$HOME/.config/qtile/autostart.sh"
PYWAL_JSON="$HOME/.cache/wal/colors.json"

# ==============================================================================
# 1. WALLPAPER SELECTION VIA ROFI
# ==============================================================================
if [ ! -d "$WALLPAPER_DIR" ]; then
    notify-send "Rice Script" "Error: Wallpaper folder '$WALLPAPER_DIR' does not exist."
    exit 1
fi

SELECTED_WALL=$(cd "$WALLPAPER_DIR" && ls | rofi -dmenu -i -p " Select Wallpaper:")

if [ -z "$SELECTED_WALL" ]; then
    exit 0
fi

FULL_WALL_PATH="$WALLPAPER_DIR/$SELECTED_WALL"

# ==============================================================================
# 2. SAFE BACKUP (Organized Directory Format)
# ==============================================================================
BACKUP_TIME=$(date +%H-%M-%S)
BACKUP_DIR="$HOME/backups/LINUX_CONFIG_BACKUPS/qtile-rice-backup-$BACKUP_TIME.bk"

mkdir -p "$BACKUP_DIR"

[ -f "$ALACRITTY_CONF" ] && cp "$ALACRITTY_CONF" "$BACKUP_DIR/alacritty.toml"
[ -f "$QTILE_CONF" ]     && cp "$QTILE_CONF"     "$BACKUP_DIR/config.py"
[ -f "$QTILE_AUTOSTART" ]&& cp "$QTILE_AUTOSTART" "$BACKUP_DIR/autostart.sh"

# ==============================================================================
# 3. PYWAL PROCESSING
# ==============================================================================
wal -i "$FULL_WALL_PATH"

if [ ! -f "$PYWAL_JSON" ]; then
    notify-send "Rice Script" "Error: Pywal cache JSON not found."
    exit 1
fi

get_color() {
    grep -Po "\"$1\": \"\K[^\"]*" "$PYWAL_JSON"
}

FG=$(get_color "foreground")
C1=$(get_color "color1")
C2=$(get_color "color2")
C3=$(get_color "color3")
C4=$(get_color "color4")
C5=$(get_color "color5")
C6=$(get_color "color6")
C7=$(get_color "color7")
C8=$(get_color "color8")
C9=$(get_color "color9")
C10=$(get_color "color10")
C11=$(get_color "color11")
C12=$(get_color "color12")
C13=$(get_color "color13")
C14=$(get_color "color14")
C15=$(get_color "color15")

# ==============================================================================
# 4. INLINE SED REPLACEMENT (Alacritty, Qtile Border, & Feh Wallpaper)
# ==============================================================================

# Update Feh wallpaper command inside autostart.sh
if [ -f "$QTILE_AUTOSTART" ]; then
    sed -i "s|^[[:space:]]*feh[[:space:]]*--bg-fill[[:space:]]*.*|feh --bg-fill $FULL_WALL_PATH|g" "$QTILE_AUTOSTART"
fi

# Update Qtile screen border color using the dominant Pywal color ($C1)
if [ -f "$QTILE_CONF" ]; then
    #sed -i "s|this_current_screen_border[[:space:]]*=[[:space:]]*\"#[^\"]*\"|this_current_screen_border=\"$C1\"|g" "$QTILE_CONF"
fi

# Update colors inside [colors.primary] block
sed -i "/\[colors\.primary\]/,/^[[:space:]]*$/ { s|background[[:space:]]*=[[:space:]]*\"#[^\"]*\"|background = \"#000000\"|g; s|foreground[[:space:]]*=[[:space:]]*\"#[^\"]*\"|foreground = \"$FG\"|g }" "$ALACRITTY_CONF"

# Update colors inside [colors.cursor] block
sed -i "/\[colors\.cursor\]/,/^[[:space:]]*$/ { s|cursor[[:space:]]*=[[:space:]]*\"#[^\"]*\"|cursor = \"$FG\"|g }" "$ALACRITTY_CONF"

# Update colors inside [colors.normal] block
sed -i "/\[colors\.normal\]/,/^[[:space:]]*$/ {
    s|black[[:space:]]*=[[:space:]]*\"#[^\"]*\"|black = \"#000000\"|g
    s|red[[:space:]]*=[[:space:]]*\"#[^\"]*\"|red = \"$C1\"|g
    s|green[[:space:]]*=[[:space:]]*\"#[^\"]*\"|green = \"$C2\"|g
    s|yellow[[:space:]]*=[[:space:]]*\"#[^\"]*\"|yellow = \"$C3\"|g
    s|blue[[:space:]]*=[[:space:]]*\"#[^\"]*\"|blue = \"$C4\"|g
    s|magenta[[:space:]]*=[[:space:]]*\"#[^\"]*\"|magenta = \"$C5\"|g
    s|cyan[[:space:]]*=[[:space:]]*\"#[^\"]*\"|cyan = \"$C6\"|g
    s|white[[:space:]]*=[[:space:]]*\"#[^\"]*\"|white = \"$C7\"|g
}" "$ALACRITTY_CONF"

# Update colors inside [colors.bright] block
sed -i "/\[colors\.bright\]/,/^[[:space:]]*$/ {
    s|black[[:space:]]*=[[:space:]]*\"#[^\"]*\"|black = \"$C8\"|g
    s|red[[:space:]]*=[[:space:]]*\"#[^\"]*\"|red = \"$C9\"|g
    s|green[[:space:]]*=[[:space:]]*\"#[^\"]*\"|green = \"$C10\"|g
    s|yellow[[:space:]]*=[[:space:]]*\"#[^\"]*\"|yellow = \"$C11\"|g
    s|blue[[:space:]]*=[[:space:]]*\"#[^\"]*\"|blue = \"$C12\"|g
    s|magenta[[:space:]]*=[[:space:]]*\"#[^\"]*\"|magenta = \"$C13\"|g
    s|cyan[[:space:]]*=[[:space:]]*\"#[^\"]*\"|cyan = \"$C14\"|g
    s|white[[:space:]]*=[[:space:]]*\"#[^\"]*\"|white = \"$C15\"|g
}" "$ALACRITTY_CONF"

notify-send "Rice Complete" "Applied: $SELECTED_WALL (Inline Replacement Done)"
