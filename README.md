# Resume Builder MVP

This is a Django + React project for building customizable, modular digital resumes. It's designed to allow non-technical users ("applicants") to configure how their resume appears, while giving developers the flexibility to extend and theme the system if they choose to fork it.

---

## 🧠 Project Goals

- ✅ Build a personal-use digital resume tool
- ✅ Serve as a real-world, full-stack portfolio piece
- ✅ Balance extensibility with MVP pragmatism
- ✅ Allow future forking by others with clean architecture
---

### 📦 Plan & Subscription Enforcement
- Record creation and retrieval are capped based on applicant's current subscription plan
- Limits are enforced in both model mixins and DRF view mixins

---

## 🛠️ Tech Stack

### Backend
- Django 4+
- Django REST Framework
- PostgreSQL
- Redis (for caching)
- ContentType framework (for plan-aware limits)

### Frontend
- React + TypeScript
- React-Bootstrap
- Axios

---

## 🧩 Architecture Overview

### View Logic
- DRF views for each widget respect plan-based record limits
- Prefetch queries are capped based on subscription

---

## 🗃️ Developer Notes

### Deferred Features (Commented/Planned, not Implemented)
- Per-widget theming via `advanced_config`
- AI-powered resume assistant
- Resume is rendered by grouping widgets by page region
- `Page`, `Widget`, `PageWidget`: Developer-defined layout
- `ApplicantWidget`: Applicant-defined widget preferences (visibility, order)
- `WidgetInstanceOption`: Optional per-widget config for advanced users

These are intentionally deferred to keep the MVP focused and deployable. The architecture supports them cleanly if added later.

### Design Philosophy
> "Is this necessary for the user right now, or just satisfying for the engineer in me?"

This principle guided what got built and what got commented.

---

## 🧪 Local Dev

```bash
# Backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend
cd frontend
npm install
npm start
```
---

## 📎 License
The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## 🙏 Thanks
Built by a developer for developers — with clean separation between dev flexibility and non-technical user UX.

DMs welcome if you fork it and make something cool!

