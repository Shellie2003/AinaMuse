import flet as ft

# ─────────────────────────────────────────────────────────────
# 1. MUSIC THEORY DATA & FULL CHORD DATABASE
# ─────────────────────────────────────────────────────────────
NOTES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

ENHARMONIC = {
    "A#": "Bb", "D#": "Eb", "G#": "Ab",
    "Db": "C#", "Gb": "F#", "Cb": "B", "Fb": "E",
}

COMMON_CHORDS = [
    ("C Major",  "A"), ("D Major",  "B"), ("E Major",  "C#"),
    ("F Major",  "D"), ("G Major",  "E"), ("A Major",  "F#"),
    ("B Major",  "Ab"), ("C# Major", "Bb"), ("Eb Major", "C"),
    ("Ab Major", "F"), ("Bb Major", "G"), ("F# Major", "Eb"),
]

# Base de données COMPLÈTE des doigtés (E, A, D, G, B, e)
# Format: [("frette_de_base", "cordes_séparées_par_des_virgules")]
# "x" = muet, "0" = vide, chiffre = frette exacte
CHORD_DB = {
    # ─── MAJEURS ───
    "C Maj": [("1", "x,3,2,0,1,0"), ("3", "x,3,5,5,5,3"), ("8", "8,10,10,9,8,8")],
    "C# Maj": [("1", "x,4,3,1,2,1"), ("4", "x,4,6,6,6,4"), ("9", "9,11,11,10,9,9")],
    "D Maj": [("1", "x,x,0,2,3,2"), ("5", "x,5,7,7,7,5"), ("10", "10,12,12,11,10,10")],
    "Eb Maj": [("1", "x,x,1,3,4,3"), ("6", "x,6,8,8,8,6"), ("11", "11,13,13,12,11,11")],
    "E Maj": [("1", "0,2,2,1,0,0"), ("7", "x,7,9,9,9,7"), ("1", "x,x,6,4,5,4")],
    "F Maj": [("1", "1,3,3,2,1,1"), ("8", "x,8,10,10,10,8"), ("1", "x,x,3,2,1,1")],
    "F# Maj": [("2", "2,4,4,3,2,2"), ("9", "x,9,11,11,11,9"), ("1", "x,x,4,3,2,2")],
    "G Maj": [("1", "3,2,0,0,0,3"), ("3", "3,5,5,4,3,3"), ("10", "x,10,12,12,12,10")],
    "Ab Maj": [("4", "4,6,6,5,4,4"), ("11", "x,11,13,13,13,11"), ("1", "x,x,6,5,4,4")],
    "A Maj": [("1", "x,0,2,2,2,0"), ("5", "5,7,7,6,5,5"), ("1", "x,x,7,6,5,5")],
    "Bb Maj": [("1", "x,1,3,3,3,1"), ("6", "6,8,8,7,6,6"), ("1", "x,x,8,7,6,6")],
    "B Maj": [("2", "x,2,4,4,4,2"), ("7", "7,9,9,8,7,7"), ("1", "x,x,9,8,7,7")],

    # ─── MINEURS ───
    "C min": [("3", "x,3,5,5,4,3"), ("8", "8,10,10,8,8,8"), ("1", "x,x,1,0,1,3")],
    "C# min": [("4", "x,4,6,6,5,4"), ("9", "9,11,11,9,9,9"), ("1", "x,x,2,1,2,0")],
    "D min": [("1", "x,x,0,2,3,1"), ("5", "x,5,7,7,6,5"), ("10", "10,12,12,10,10,10")],
    "Eb min": [("6", "x,6,8,8,7,6"), ("11", "11,13,13,11,11,11"), ("1", "x,x,1,3,4,2")],
    "E min": [("1", "0,2,2,0,0,0"), ("7", "x,7,9,9,8,7"), ("1", "x,x,2,0,0,0")],
    "F min": [("1", "1,3,3,1,1,1"), ("8", "x,8,10,10,9,8"), ("1", "x,x,3,1,1,1")],
    "F# min": [("2", "2,4,4,2,2,2"), ("9", "x,9,11,11,10,9"), ("1", "x,x,4,2,2,2")],
    "G min": [("3", "3,5,5,3,3,3"), ("10", "x,10,12,12,11,10"), ("1", "x,x,5,3,3,3")],
    "Ab min": [("4", "4,6,6,4,4,4"), ("11", "x,11,13,13,12,11"), ("1", "x,x,6,4,4,4")],
    "A min": [("1", "x,0,2,2,1,0"), ("5", "5,7,7,5,5,5"), ("1", "x,x,2,2,1,0")],
    "Bb min": [("1", "x,1,3,3,2,1"), ("6", "6,8,8,6,6,6"), ("1", "x,x,3,3,2,1")],
    "B min": [("2", "x,2,4,4,3,2"), ("7", "7,9,9,7,7,7"), ("1", "x,x,9,7,7,7")],

    # ─── DIMINUÉS ───
    "C dim": [("1", "x,3,4,5,4,x"), ("8", "8,9,10,x,x,x"), ("1", "x,x,1,2,1,2")],
    "C# dim": [("4", "x,4,5,6,5,x"), ("9", "9,10,11,x,x,x"), ("1", "x,x,2,3,2,3")],
    "D dim": [("5", "x,5,6,7,6,x"), ("10", "10,11,12,x,x,x"), ("1", "x,x,0,1,3,1")],
    "Eb dim": [("6", "x,6,7,8,7,x"), ("11", "11,12,13,x,x,x"), ("1", "x,x,1,2,4,2")],
    "E dim": [("7", "x,7,8,9,8,x"), ("1", "0,1,2,0,x,x"), ("1", "x,x,2,3,5,3")],
    "F dim": [("8", "x,8,9,10,9,x"), ("1", "1,2,3,x,x,x"), ("1", "x,x,3,4,6,4")],
    "F# dim": [("9", "x,9,10,11,10,x"), ("2", "2,3,4,x,x,x"), ("1", "x,x,4,5,7,5")],
    "G dim": [("10", "x,10,11,12,11,x"), ("3", "3,4,5,x,x,x"), ("1", "x,x,5,6,8,6")],
    "Ab dim": [("11", "x,11,12,13,12,x"), ("4", "4,5,6,x,x,x"), ("1", "x,x,6,7,9,7")],
    "A dim": [("1", "x,0,1,2,1,x"), ("5", "5,6,7,x,x,x"), ("1", "x,x,7,8,10,8")],
    "Bb dim": [("1", "x,1,2,3,2,x"), ("6", "6,7,8,x,x,x"), ("1", "x,x,8,9,11,9")],
    "B dim": [("2", "x,2,3,4,3,x"), ("7", "7,8,9,x,x,x"), ("1", "x,x,9,10,12,10")],
}

saved_items: list[dict] = []

# ─────────────────────────────────────────────────────────────
# 2. LOGIC HELPERS
# ─────────────────────────────────────────────────────────────

def normalize(note: str) -> str: return ENHARMONIC.get(note, note)
def note_index(note: str) -> int: return NOTES.index(normalize(note))
def transpose_note(note: str, semitones: int) -> str: return NOTES[(note_index(note) + semitones) % 12]
def capo_fret(original: str, playing: str) -> int: return (note_index(playing) - note_index(original)) % 12
def fret_suffix(n: int) -> str: return "st" if n == 1 else "nd" if n == 2 else "rd" if n == 3 else "th"

def keyboard_semitones(original: str, playing: str) -> int:
    diff = note_index(playing) - note_index(original)
    if diff > 6: diff -= 12
    elif diff < -6: diff += 12
    return diff

def build_common_conversions(original: str, playing: str) -> list:
    semitones = capo_fret(original, playing)
    result = []
    for orig_chord, rel_minor_root in COMMON_CHORDS:
        parts = orig_chord.split()
        new_root = transpose_note(parts[0], semitones)
        result.append((orig_chord, f"{new_root} {parts[1]}"))
        new_rm = transpose_note(rel_minor_root, semitones)
        result.append((f"{rel_minor_root} Minor", f"{new_rm} Minor"))
    seen, out = set(), []
    for pair in result:
        if pair[0] not in seen: seen.add(pair[0]); out.append(pair)
    return out[:10]

def get_diatonic_chords(root_note: str) -> list:
    intervals = [0, 2, 4, 5, 7, 9, 11]
    qualities = ["Maj", "min", "min", "Maj", "Maj", "min", "dim"]
    root_idx = note_index(root_note)
    return [f"{NOTES[(root_idx + interval) % 12]} {qualities[i]}" for i, interval in enumerate(intervals)]

# ─────────────────────────────────────────────────────────────
# 3. COLORS & THEME CONSTANTS
# ─────────────────────────────────────────────────────────────
BG_DARK = "#0D1117"
BG_CARD = "#161B22"
BG_CARD2 = "#1C2333"
BG_KEY_DEFAULT = "#1E2A3A"
BG_KEY_SELECTED = "#1A6EE8"
ACCENT = "#1A6EE8"
ACCENT_LIGHT = "#4D94FF"
TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#8B949E"
TEXT_ACCENT = "#4D94FF"
DIVIDER_COLOR = "#30363D"

# ─────────────────────────────────────────────────────────────
# 4. GRAPHIC WIDGETS
# ─────────────────────────────────────────────────────────────

def draw_fretboard_graphic(start_fret: str, finger_str: str) -> ft.Container:
    """Dessine le manche et place les doigts avec la précision visuelle."""
    strings = finger_str.split(",")
    base_fret = int(start_fret)
    
    W, H = 100, 130
    S_SPACE = W / 5
    F_SPACE = H / 4 # 4 cases affichées

    layers = []
    
    # 1. Cordes Verticales
    for i in range(6):
        thickness = 2 if i == 0 or i == 5 else 1
        layers.append(ft.Container(
            bgcolor="#555555", width=thickness, height=H, left=i * S_SPACE, top=20
        ))
        
    # 2. Frettes Horizontales
    for i in range(5):
        is_nut = (i == 0 and base_fret == 1)
        layers.append(ft.Container(
            bgcolor="#ffffff" if is_nut else "#777777", 
            width=W, height=4 if is_nut else 1.5, 
            left=0, top=20 + i * F_SPACE
        ))

    # 3. Marqueurs (X, O, ou Numéro de frette)
    for i, val in enumerate(strings):
        x = i * S_SPACE
        if val.lower() == 'x':
            layers.append(ft.Text("X", size=12, color="red", weight=ft.FontWeight.BOLD, left=x - 4, top=0))
        elif val == '0':
            layers.append(ft.Text("O", size=12, color=ACCENT_LIGHT, weight=ft.FontWeight.BOLD, left=x - 5, top=0))
        elif val.isdigit():
            fret_num = int(val)
            rel_fret = (fret_num - base_fret) + 1
            if 1 <= rel_fret <= 4:
                # Centrage du point dans la case
                y = 20 + (rel_fret * F_SPACE) - (F_SPACE / 2)
                layers.append(
                    ft.Container(
                        content=ft.Text(str(fret_num), size=9, color=BG_DARK, weight=ft.FontWeight.BOLD),
                        width=18, height=18, bgcolor="white", border_radius=9,
                        alignment=ft.Alignment.CENTER,
                        left=x - 9, top=y - 9
                    )
                )

    # 4. Indicateur de frette de base sur le côté droit
    if base_fret > 1:
        layers.append(
            ft.Text(f"{base_fret}fr", size=10, italic=True, color=TEXT_SECONDARY, left=W + 6, top=20 + (F_SPACE/2) - 8)
        )

    return ft.Container(
        content=ft.Stack(controls=layers, width=W + 30, height=H + 20),
        padding=15,
        bgcolor=BG_CARD2,
        border_radius=8,
        margin=ft.Margin(0, 5, 10, 5)
    )

# ─────────────────────────────────────────────────────────────
# 5. UI BUILDERS
# ─────────────────────────────────────────────────────────────

def key_button(note: str, selected: bool, on_click) -> ft.Container:
    return ft.Container(
        content=ft.Text(note, size=14, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
        width=48, height=48, border_radius=8,
        bgcolor=BG_KEY_SELECTED if selected else BG_KEY_DEFAULT,
        alignment=ft.Alignment.CENTER, on_click=on_click, data=note,
        animate=ft.Animation(150, ft.AnimationCurve.EASE_OUT),
    )

def section_label(text: str, subtitle: str = "") -> ft.Row:
    children = [ft.Text(text, size=13, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY)]
    if subtitle: children.append(ft.Text(subtitle, size=12, color=TEXT_ACCENT, italic=True))
    return ft.Row(controls=children, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

def result_card(icon_name, title: str, value: str, unit: str, description: str) -> ft.Container:
    return ft.Container(
        content=ft.Column([
            ft.Row([ft.Container(content=ft.Icon(icon_name, color=ACCENT_LIGHT, size=18), margin=ft.Margin(0,0,6,0)), ft.Text(title, size=11, weight=ft.FontWeight.BOLD, color=TEXT_SECONDARY)]),
            ft.Row([ft.Text(value, size=52, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY), ft.Text(unit, size=18, weight=ft.FontWeight.W_600, color=ACCENT_LIGHT)], vertical_alignment=ft.CrossAxisAlignment.END),
            ft.Text(description, size=12, color=TEXT_SECONDARY),
        ], spacing=4),
        padding=18, bgcolor=BG_CARD, border_radius=12, border=ft.Border.all(1, DIVIDER_COLOR)
    )

# ─────────────────────────────────────────────────────────────
# 6. PAGES
# ─────────────────────────────────────────────────────────────

def calculator_page(page: ft.Page, state: dict, on_change) -> ft.Column:
    orig = state["original"]
    play = state["playing"]
    selected_chord = state.get("selected_chord")
    fret = capo_fret(orig, play)
    semi = keyboard_semitones(orig, play)
    conversions = build_common_conversions(orig, play)
    direction = "up" if semi >= 0 else "down"
    semi_abs = abs(semi)
    sfx = fret_suffix(fret)
    
    diatonic_chords = get_diatonic_chords(play)

    def make_buttons(current_val: str, key_type: str):
        buttons = [key_button(n, n == current_val, lambda e, note=n: on_change(key_type, note)) for n in NOTES]
        return ft.Row(controls=buttons[:6], spacing=6, scroll=ft.ScrollMode.HIDDEN), ft.Row(controls=buttons[6:], spacing=6, scroll=ft.ScrollMode.HIDDEN)

    orig_row1, orig_row2 = make_buttons(orig, "original")
    play_row1, play_row2 = make_buttons(play, "playing")

    # Logique pour afficher les positions si un accord est sélectionné
    fret_visuals = ft.Container()
    if selected_chord:
        # On normalise le nom pour matcher la DB
        chord_key = selected_chord.replace("Major", "Maj").replace("Minor", "min")
        variations = CHORD_DB.get(chord_key, [("1", "x,x,x,x,x,x")])
        
        fret_visuals = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(f"FRETBOARD POSITIONS: {selected_chord.upper()}", size=12, weight=ft.FontWeight.BOLD, color=ACCENT_LIGHT),
                    ft.IconButton(icon=ft.Icons.CLOSE, icon_color=TEXT_SECONDARY, icon_size=16, on_click=lambda e: on_change("select_chord", None))
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Row([draw_fretboard_graphic(v[0], v[1]) for v in variations], scroll=ft.ScrollMode.AUTO)
            ]),
            padding=15, bgcolor=BG_CARD, border_radius=12, border=ft.Border.all(1, DIVIDER_COLOR),
            margin=ft.Margin(0, 0, 0, 20)
        )

    conv_rows = []
    for orig_chord, new_chord in conversions:
        conv_rows.append(ft.Row([ft.Text(orig_chord, size=13, color=TEXT_SECONDARY, expand=True), ft.Text(new_chord, size=13, color=ACCENT_LIGHT, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN))
        conv_rows.append(ft.Divider(height=1, color=DIVIDER_COLOR))

    border_all = ft.Border(left=ft.BorderSide(1, DIVIDER_COLOR), right=ft.BorderSide(1, DIVIDER_COLOR), top=ft.BorderSide(1, DIVIDER_COLOR), bottom=ft.BorderSide(1, DIVIDER_COLOR))

    return ft.Column(
        controls=[
            ft.Container(height=8),
            section_label("SONG KEY (ORIGINALE)", "Select One"),
            ft.Container(height=8),
            orig_row1,
            ft.Container(height=6),
            orig_row2,
            ft.Container(height=16),

            section_label("PLAYING KEY (JOUÉE)", "Relative to neck"),
            ft.Container(height=8),
            play_row1,
            ft.Container(height=6),
            play_row2,
            ft.Container(height=16),

            # Progression section
            section_label(f"PLAYING KEY PROGRESSION ({play} Major)", "Tap chord for diagrams"),
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(chord, size=12, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                            padding=10, bgcolor=ACCENT if selected_chord == chord else BG_CARD2, border_radius=8,
                            on_click=lambda e, c=chord: on_change("select_chord", c)
                        ) for chord in diatonic_chords
                    ],
                    scroll=ft.ScrollMode.AUTO
                ),
                padding=10, bgcolor=BG_CARD, border_radius=12, border=border_all
            ),
            ft.Container(height=16),
            
            fret_visuals, # Affichage dynamique des variations de l'accord sélectionné

            result_card(ft.Icons.PIANO, "GUITAR CAPO", str(fret), f"{sfx} Fret", f"Place capo on {fret}{sfx} fret of the neck"),
            ft.Container(height=12),
            result_card(ft.Icons.QUEUE_MUSIC, "KEYBOARD TRANSPOSE", f"+{semi_abs}" if semi >= 0 else f"-{semi_abs}", "st", f"Shift settings by {semi_abs} semitones {direction}"),
            ft.Container(height=20),

            ft.Text("COMMON CONVERSIONS", size=11, weight=ft.FontWeight.BOLD, color=TEXT_SECONDARY),
            ft.Container(height=8),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row([ft.Text("Original", size=13, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY, expand=True), ft.Text("New Chord", size=13, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Divider(height=1, color=DIVIDER_COLOR),
                        *conv_rows,
                    ], spacing=4
                ),
                padding=ft.Padding(14, 14, 14, 14), bgcolor=BG_CARD, border_radius=ft.BorderRadius(12, 12, 12, 12), border=border_all,
            ),
            ft.Container(height=24),
            ft.Container(
                content=ft.Button(
                    content=ft.Text("Save this calculation"), icon=ft.Icons.BOOKMARK_ADD_OUTLINED, bgcolor=ACCENT, color=TEXT_PRIMARY, width=300,
                    on_click=lambda e: on_change("save", None), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                ),
                alignment=ft.Alignment.CENTER,
            ),
            ft.Container(height=24),
        ],
        spacing=0,
        scroll=ft.ScrollMode.AUTO
    )

def saved_page(page: ft.Page, state: dict, on_delete) -> ft.Column:
    border_all = ft.Border.all(1, DIVIDER_COLOR)

    if not saved_items:
        return ft.Column(
            controls=[
                ft.Container(height=60),
                ft.Column(
                    controls=[
                        ft.Icon(ft.Icons.BOOKMARK_BORDER, color=TEXT_SECONDARY, size=64),
                        ft.Container(height=16),
                        ft.Text("No saved calculations", size=16, color=TEXT_SECONDARY, weight=ft.FontWeight.W_500),
                        ft.Text("Use the Calculator tab and save your results.", size=13, color=TEXT_SECONDARY),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=6,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        )

    items = []
    for i, item in enumerate(saved_items):
        f, semi = item["fret"], item["semi"]
        sfx, sign = fret_suffix(f), "+" if semi >= 0 else ""
        items.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row([ft.Text(f'{item["orig"]} → {item["play"]}', size=15, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY), ft.IconButton(icon=ft.Icons.DELETE_OUTLINE, icon_color=TEXT_SECONDARY, icon_size=18, on_click=lambda e, idx=i: on_delete(idx))], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Row([
                            ft.Container(content=ft.Text(f"Capo: {f}{sfx} fret", size=12, color=ACCENT_LIGHT), bgcolor=f"{ACCENT}33", padding=ft.Padding(10, 4, 10, 4), border_radius=ft.BorderRadius(20, 20, 20, 20)),
                            ft.Container(content=ft.Text(f"Transpose: {sign}{semi}st", size=12, color=ACCENT_LIGHT), bgcolor=f"{ACCENT}33", padding=ft.Padding(10, 4, 10, 4), border_radius=ft.BorderRadius(20, 20, 20, 20)),
                        ], spacing=8),
                    ], spacing=8
                ),
                padding=ft.Padding(14, 14, 14, 14), bgcolor=BG_CARD, border_radius=ft.BorderRadius(12, 12, 12, 12), border=border_all, margin=ft.Margin(0, 0, 0, 10)
            )
        )

    return ft.Column([
        ft.Container(height=8),
        ft.Text(f"{len(saved_items)} saved calculation{'s' if len(saved_items)!=1 else ''}", size=13, color=TEXT_SECONDARY),
        ft.Container(height=12),
        *items,
        ft.Container(height=24),
    ], spacing=0, scroll=ft.ScrollMode.AUTO)

def show_info_dialog(page: ft.Page):
    dlg = ft.AlertDialog(
        modal=True, title=ft.Text("AinaMuse", weight=ft.FontWeight.BOLD),
        content=ft.Column([
            ft.Text("Guitar Capo & Keyboard Transpose Calculator", color=TEXT_SECONDARY, size=13),
            ft.Container(height=10),
            ft.Text("How to use:", weight=ft.FontWeight.BOLD, size=13),
            ft.Text("1. Select the ORIGINAL song key", size=13),
            ft.Text("2. Select the PLAYING key (capo/transpose target)", size=13),
            ft.Text("3. Read the Guitar Capo fret and Keyboard semitones", size=13),
            ft.Container(height=10),
            ft.Text("Version 1.0 • Powered by AinaDigit", color=TEXT_SECONDARY, size=11),
        ], spacing=4, tight=True),
        actions=[ft.TextButton("Close", on_click=lambda e: close_dialog(page, dlg))],
        bgcolor=BG_CARD2,
    )
    page.dialog = dlg
    dlg.open = True
    page.update()

def close_dialog(page: ft.Page, dlg):
    dlg.open = False
    page.update()

def show_settings_dialog(page: ft.Page, state: dict, on_theme_change):
    use_flats = state.get("use_flats", True)
    dlg = ft.AlertDialog(
        modal=True, title=ft.Text("Settings", weight=ft.FontWeight.BOLD),
        content=ft.Column([
            ft.Text("Accidentals display:", size=13),
            ft.RadioGroup(
                content=ft.Column([ft.Radio(value="flats", label="Flats (Eb, Ab, Bb)"), ft.Radio(value="sharps", label="Sharps (D#, G#, A#)")]),
                value="flats" if use_flats else "sharps",
                on_change=lambda e: on_theme_change("use_flats", e.control.value == "flats"),
            ),
        ], spacing=8, tight=True),
        actions=[ft.TextButton("Close", on_click=lambda e: close_dialog(page, dlg))],
        bgcolor=BG_CARD2,
    )
    page.dialog = dlg
    dlg.open = True
    page.update()

# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

def main(page: ft.Page):
    page.title = "AinaMuse"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = BG_DARK
    page.padding = ft.Padding(16, 0, 16, 0)

    state = {"original": "C", "playing": "G", "tab": 0, "use_flats": True, "selected_chord": None}

    content_col = ft.Column(expand=True, scroll=ft.ScrollMode.HIDDEN, spacing=0)

    def rebuild():
        content_col.controls.clear()
        if state["tab"] == 0:
            content_col.controls.append(calculator_page(page, state, handle_change))
        else:
            content_col.controls.append(saved_page(page, state, handle_delete_saved))
        page.update()

    def handle_change(key: str, value):
        if key == "save":
            saved_items.append({"orig": state["original"], "play": state["playing"], "fret": capo_fret(state["original"], state["playing"]), "semi": keyboard_semitones(state["original"], state["playing"])})
            page.snack_bar = ft.SnackBar(content=ft.Text("Calculation saved!", color=TEXT_PRIMARY), bgcolor=ACCENT, duration=2000)
            page.snack_bar.open = True
            page.update()
            return
        elif key == "select_chord":
            state["selected_chord"] = value
        else:
            state[key] = value
            state["selected_chord"] = None
        rebuild()

    def handle_delete_saved(idx: int):
        if 0 <= idx < len(saved_items): saved_items.pop(idx)
        rebuild()

    def handle_tab_change(e: ft.ControlEvent):
        state["tab"] = e.control.selected_index
        rebuild()

    def handle_settings(e):
        show_settings_dialog(page, state, lambda k, v: (state.update({k: v}), page.update()))

    page.appbar = ft.AppBar(
        leading=ft.IconButton(icon=ft.Icons.SETTINGS_OUTLINED, icon_color=TEXT_PRIMARY, icon_size=22, on_click=handle_settings),
        leading_width=48, title=ft.Text("AinaMuse", size=18, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
        center_title=True, bgcolor=BG_DARK,
        actions=[ft.IconButton(icon=ft.Icons.INFO_OUTLINE, icon_color=TEXT_PRIMARY, icon_size=22, on_click=lambda e: show_info_dialog(page))],
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.CALCULATE_OUTLINED, selected_icon=ft.Icons.CALCULATE, label="Calculator"),
            ft.NavigationBarDestination(icon=ft.Icons.BOOKMARK_BORDER, selected_icon=ft.Icons.BOOKMARK, label="Saved"),
        ],
        selected_index=0, bgcolor=BG_DARK, indicator_color=f"{ACCENT}55",
        label_behavior=ft.NavigationBarLabelBehavior.ALWAYS_SHOW, on_change=handle_tab_change,
    )

    page.add(content_col)
    rebuild()

ft.run(main)