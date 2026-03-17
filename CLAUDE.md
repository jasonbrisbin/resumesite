## Description
This project publishes my resume to a static website hosted on Azure. The workflow consists of taking ./src/content.yaml and converting it into a static site which is published to https://jasonbrisbin.com.

## Iconography
Use Font Awesome 5.15.3 icons for the contact information section in the hero header.

## Source
The resume is defined as a YAML file at ./src/content.yaml. Use this file to generate static HTML via the Jinja2 template at ./src/template.html.

## Workflow
After any formatting or content change, always prompt me to run the /build command and then open dist/index.html in the browser so I can preview the result.

## Design

### Style
Clean and minimal. Lots of whitespace, subtle typography, professional and timeless.

### Layout
Single-column, full-width scrollable page. Max content width: 900px, centered on a gray (#d0d0d0) page background with a subtle box-shadow.

### Colors
- Gold: #e2bf2b (accents, dates, section title underlines, profile left border)
- Purple: #4a1e9e (badges, job titles, hover states)
- Hero background: rgba(74, 30, 158, 0.75) — original purple at 75% opacity
- Text: #2d2d2d (dark), #666666 (muted), #888888 (subtle)
- Background: #ffffff (content), #f8f8f9 (bottom grid alt)
- Border: #e8e8e8

### Fonts
- Headings: Oswald (400, 600) — used for hero name and section titles
- Body: Inter (300, 400, 500, 600, 700) — replaced Roboto for better screen readability

### Hero Header
- Purple background (rgba), single row: circular headshot left, name/title/contacts right
- Headshot: 120px circle, 2px gold gradient border (gold at top fading to transparent at 80%)
- Border uses CSS gradient trick: `border: 2px solid transparent` + `background: padding-box / border-box` layers
- Name: gold first name + white last name (Oswald 600, uppercase, clamp 2rem–3.2rem)
- Subtitle: "Senior DevOps Engineer" in small uppercase muted text
- Contacts: flex-wrap row with gold FA icons

### Section Titles
Small (0.85rem), uppercase, muted gray, Oswald — act as category labels (modern "eyebrow" style)
Gold 2px bottom border on the title text itself (inline-block)

### Profile Section
Gold 2px left border with padding-left. Text is italic, 1rem, line-height 1.8, dark color.

### Experience Section
- Employer name: Oswald uppercase, job position title: purple uppercase 0.9rem
- Dates: gold 0.8rem
- Position entries indented with `border-left: 2px solid #e8e8e8` (timeline effect)
- Bullet points use gold 5px circle markers
- Badges: purple filled, white text, border-radius 3px, 0.72rem

### Skills Section
Family name label (min-width 130px) + flex-wrap outlined tags. Tags hover to purple fill.

### Bottom Section (Certificates + Education)
- Single column stack, light gray background (#f8f8f9)
- Certificates first, then Education
- Font style matches: 0.9375rem, font-weight 600, color #2d2d2d — same as education course title
- No checkmark icons on certificates

### Career Focus
The resume targets roles at the intersection of DevOps and Artificial Intelligence — specifically enabling engineering teams to deliver faster and build more resilient solutions through intelligent automation and AI-assisted tooling.
