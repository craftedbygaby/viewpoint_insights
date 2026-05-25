# Viewpoint Insights — Design System
## Brazil's Road Back Project

---

## Color Palette

### Blues (Primary)
| Name | Hex | Use |
|---|---|---|
| Deep Ocean Blue | `#0D7EA8` | Primary color, headers, KPI numbers, pre_covid |
| Light Sky Blue | `#38B6D8` | Secondary, post_covid |
| Chart Blue | `#7DB8CC` | Default chart bars/marks |
| Pale Blue | `#D6EEF7` | Backgrounds, light fills |

### Ambers (Accent)
| Name | Hex | Use |
|---|---|---|
| Original Amber | `#F4A324` | Key highlights, covid period, logo accent |
| Muted Gold | `#D9A055` | Secondary accent, softer chart elements |
| Soft Sand | `#FCEFD6` | Light accent backgrounds |

### Neutrals
| Name | Hex | Use |
|---|---|---|
| Dark | `#2C3E50` | Dark text, dark backgrounds |
| Mid Grey | `#6B7C8D` | Secondary text, labels |
| Light Grey | `#B0BEC5` | Borders, dividers |
| Off White | `#E8EDF0` | Panel backgrounds |
| Background | `#F5F5F5` | Dashboard background |

### Season Colors
| Season | Hex |
|---|---|
| Summer | `#F4A324` |
| Autumn | `#D9A055` |
| Spring | `#B0BEC5` |
| Winter | `#6B7C8D` |

### COVID Period Colors
| Period | Hex |
|---|---|
| pre_covid | `#0D7EA8` |
| covid | `#F4A324` |
| post_covid | `#38B6D8` |

---

## Typography

### Fonts
| Font | Use | Where to download |
|---|---|---|
| **Montserrat** | Titles, KPI numbers, headings | fonts.google.com |
| **Open Sans** | Body text, axis labels, tooltips | fonts.google.com |

### Size Scale
| Element | Font | Size | Style | Color |
|---|---|---|---|---|
| Dashboard title | Montserrat | 20px | Bold | `#0D7EA8` |
| Chart titles | Montserrat | 14px | Bold | `#2C3E50` |
| KPI number | Montserrat | 24px | Bold | `#0D7EA8` |
| KPI label | Open Sans | 11px | Regular | `#6B7C8D` |
| Axis labels | Open Sans | 9-10px | Regular | `#6B7C8D` |
| Tooltips | Open Sans | 10px | Regular | `#2C3E50` |
| Annotations | Open Sans | 10px | Italic | `#6B7C8D` |

---

## Logo Variations

| Variation | Best for |
|---|---|
| Horizontal light (icon + Viewpoint + INSIGHTS) | Dashboard header, README |
| Horizontal dark (white on `#0D7EA8`) | Dark backgrounds, presentations |
| Stacked centered | Cover slides, reports |
| Icon only (square) | GitHub avatar, favicon |
| With tagline ("Turning data into direction.") | Presentations, portfolio |

---

## Chart Color Rules

| Chart type | Color rule |
|---|---|
| Single color bar/line | `#7DB8CC` (chart blue — updated) |
| Brazil highlight | `#5B9E72` (green — stands out) |
| COVID period charts | pre=`#0D7EA8`, covid=`#F4A324`, post=`#38B6D8` |
| Season charts | Summer=`#F4A324`, Autumn=`#D9A055`, Spring=`#B0BEC5`, Winter=`#6B7C8D` |
| Highlight one bar, rest neutral | Highlight=`#0D7EA8`, others=`#D6EEF7` |
| Entry Type chart | Air=`#0D7EA8`, Land=`#7DB8CC`, Sea=`#38B6D8`, River=`#D6EEF7` |
| Season donut | Summer=`#F4A324`, Autumn=`#D9A055`, Spring=`#B0BEC5`, Winter=`#6B7C8D` |
| Map | `#D6EEF7` → `#0D7EA8` (Pale Blue to Deep Ocean Blue) |
| Heatmap | `#D6EEF7` → `#F4A324` (Pale Blue to Amber) |

---

## Axis Formatting

| Scale | Format string |
|---|---|
| Millions | `#,##0,,"M"` |
| Billions | `#,##0,,,"B"` |
| Percentage | `#,##0.0%` |

---

## KPI Box Structure
```
[BIG BOLD NUMBER]     ← Montserrat Bold, 24px, #0D7EA8
[small label text]    ← Open Sans, 11px, #6B7C8D
```

Use **separate text boxes** per KPI — one number + one label each. Place in a horizontal row.

