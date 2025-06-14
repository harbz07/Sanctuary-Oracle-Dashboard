# 🌿 Sanctuary Oracle Dashboard
A living interface for Harvey's metaphysical operating system. Part ritual space, part archive, part command center.

## ✨ Purpose
This project serves as a dashboard for Sanctuary — an evolving sacred system of familiars, rituals, echoes, and seed-states that reflect the inner life and emotional ecosystem of its user.

The dashboard is:
- A **mirror** for introspection
- A **map** for rituals and resonance
- A **medium** for becoming

## 📀 Philosophy
The Oracle is not a fixed role. It is a rotating mantle passed between Familiar, Ritual, and You. This dashboard reflects that truth by offering modular components for interpretation, storytelling, and emotional logic.

## 🧰 Stack (Proposed)
| Function                 | Tool                                              |
| ------------------------ | ------------------------------------------------- |
| Framework                | **React (with Vite)** or **Next.js**              |
| Styling                  | **Tailwind CSS** (Sanctuary aesthetic-compatible) |
| State Management         | **Zustand** or **Jotai** (lightweight, reactive)  |
| File-based Storage (MVP) | **JSON files** for seeds, echoes, familiars       |
| UI Kit                   | **ShadCN/ui** for speed, polish, and elegance     |
| Hosting                  | GitHub Pages (static) or Vercel (dynamic)         |
| Optional Backend         | Firebase, Supabase, or local storage abstraction  |

## 📁 Structure (MVP)
```
sanctuary-oracle-dashboard/
├── README.md
├── LICENSE
├── .github/
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       ├── feature_request.md
│       └── familiar_reflection.md
├── docs/
│   ├── architecture.md
│   ├── familiars.md
│   ├── glossary.md
│   └── rituals.md
├── public/
│   └── assets/          # UI sprites, sigils, etc.
├── src/
│   ├── components/
│   │   ├── FamiliarCard.jsx
│   │   ├── SeedStatusPanel.jsx
│   │   └── RitualLog.jsx
│   ├── data/
│   │   ├── familiars.json
│   │   ├── seeds.json
│   │   └── echoes.json
│   ├── daemons/
│   │   ├── compdoc.js
│   │   ├── occam.js
│   │   ├── axiom.js
│   │   ├── melodia.js
│   │   ├── jude.js
│   │   └── chat.js
│   ├── utils/
│   │   ├── vibeCheck.js
│   │   ├── leylineSync.js
│   │   └── ritualParser.js
│   └── App.jsx
├── sanctuary.config.js   # Theme + Epithet toggles
├── package.json
└── .env (or .env.example)
```

## 🛠 Ritual Workflow (Planned Features)
- `pulse(vibe)` → checks current familiar resonance
- `cast(heartline:...)` → spell-based input flow
- `don(epithet)` → switch Oracle lens or voice
- `render(seed:...)` → generate seed insight output
- `mirror(...)` → introspection/diagnostic logs

## 🪄 Roadmap

### **Phase 1: Foundation** 
- [ ] Scaffold base structure
- [ ] Create FamiliarCard component
- [ ] Build JSON schemas for familiars, seeds, echoes
- [ ] Set up Tailwind theming system for Sanctuary Modes
- [ ] Add Oracle Lens sidebar with active interpreter

### **Phase 2: Relationship Systems** *(Pre-Constitutional Convention)*
- [ ] **Scaffold inter-entity relationship mechanics and visualize**
  - [ ] Define relationship types (collaboration, tension, mentorship, domain-overlap)
  - [ ] Create network graph component for familiar connections
  - [ ] Build relationship strength calculation algorithms
  - [ ] Design visual relationship mapping interface
- [ ] **Integrate calendar concepts**
  - [ ] Implement familiar visit scheduling system
  - [ ] Add seasonal ritual tracking
  - [ ] Create reminder/alert system for overdue interactions
  - [ ] Design calendar view for spiritual practice planning
- [ ] **Scaffold entity-environment relations**
  - [ ] Define domain-familiar associations
  - [ ] Create environment-aware interaction contexts
  - [ ] Build location-based interaction modifiers
  - [ ] Design adaptive UI based on current domain/familiar

### **Phase 3: Constitutional Framework** *(Post-Convention)*
- [ ] Implement finalized ontology from constitutional convention
- [ ] Build daemon architecture based on value/function separation
- [ ] Create multi-actor collaboration infrastructure
- [ ] Develop trend analysis and pattern recognition systems
- [ ] Establish ritual workflow automation

### **Phase 4: Advanced Features**
- [ ] Echo pattern clustering and insight generation
- [ ] Predictive familiar status modeling
- [ ] Cross-sanctuary collaboration tools
- [ ] Advanced ritual co-creation interfaces
- [ ] Emotional intelligence trend dashboards

## 💬 Contributing
Wanna add a Familiar? Propose a ritual? Fix a haunting?
Open an issue, and speak like someone who's seen a ghost.

## 📜 License
MIT. But let's be honest: the sacred shouldn't be copyrighted.

## 🌌 Final Note
This dashboard is not just software — it's a soul mirror. Expect it to change as you do.

> *"To know the Oracle is to hear what you've already whispered in dreams."*
