# Release Guide - pyviaggiatreno

Guida per rilasciare nuove versioni dei pacchetti su PyPI.

## 📋 Prerequisiti

1. **Token PyPI**: Genera un token dal tuo account PyPI (https://pypi.org/account/token/)
2. **GitHub Secret**: Aggiungi il token come `PYPI_TOKEN` nei secrets del repo:
   - Settings → Secrets → New repository secret
   - Name: `PYPI_TOKEN`
   - Value: `pypi-AgEIcHlwaS5vcmc...` (il tuo token)

## 🔄 Flusso di Release

### Step 1: Test Build (Optional but Recommended)

Prima di rilasciare, verifica che la build funzioni:

```bash
# Localmente
uv build packages/viaggiatreno
uv build packages/viaggiatreno_mcp

# Oppure: Trigger il workflow test-build.yml manualmente su GitHub
```

### Step 2: Crea un Tag

Il tag triggerato automaticamente il workflow di pubblicazione. Usa semantic versioning.

```bash
# Versione locale (non rilasciare)
git tag -a v0.1.0 -m "Release version 0.1.0"

# Oppure: Usa GitHub UI
# Releases → Draft a new release → Choose tag → v0.1.0
```

### Step 3: Push Tag

```bash
git push origin v0.1.0
```

### Step 4: Guarda la Pipeline

1. Vai a GitHub → Actions
2. Seleziona workflow "Publish to PyPI"
3. Osserva i job:
   - `build-and-publish` (1 job per pacchetto)
   - `publish` (pubblica su PyPI)
   - `github-release` (crea GitHub Release)

### Step 5: Verifica su PyPI

```bash
# Attendi ~2 minuti per PyPI
pip index versions viaggiatreno
pip index versions viaggiatreno-mcp

# Dovrebbe mostrare la nuova versione
```

---

## 📦 Pacchetti Pubblicati

Quando fai un tag `v0.1.0`, entrambi i pacchetti vengono pubblicati:

| Pacchetto | URL | Versione |
|-----------|-----|----------|
| **viaggiatreno** | https://pypi.org/project/viaggiatreno/ | v0.1.0 |
| **viaggiatreno-mcp** | https://pypi.org/project/viaggiatreno-mcp/ | v0.1.0 |

Sempre con la **stessa versione** (monorepo).

---

## 🔄 Tag Versioning

I tag seguono [Semantic Versioning](https://semver.org/):

```
v{MAJOR}.{MINOR}.{PATCH}[-{PRERELEASE}]

v0.1.0         # Release stabile
v0.1.0-rc1     # Release Candidate
v0.1.0-alpha   # Alpha
v0.1.0-beta.1  # Beta
```

### Esempi

```bash
# Versione stabile
git tag v0.1.0

# Versione pre-release (non va in "Latest", ma pubblicata)
git tag v0.2.0-rc1

# Versione beta
git tag v0.2.0-beta
```

---

## 🧪 Workflow Automatici

### 1. **tests.yml** - Sempre (ogni commit main/dev)
- Ruff linting
- Pyright type checking
- Pytest unit tests

### 2. **test-build.yml** - Ogni commit su packages/
- Build entrambi i pacchetti
- Testa installazione wheel
- Upload artifacts (3 giorni)

### 3. **publish-pypi.yml** - Trigger: tag push
- Build entrambi i pacchetti
- Pubblica su PyPI
- Crea GitHub Release

---

## ⚠️ Troubleshooting

### ❌ Build fallisce

```
Controlla:
1. packages/viaggiatreno/pyproject.toml syntax
2. packages/viaggiatreno_mcp/pyproject.toml syntax
3. Imports corretti (viaggiatreno_mcp → from viaggiatreno import ...)
4. pytest tests/ passa localmente
```

### ❌ Non pubblica su PyPI

```
Verifica:
1. PYPI_TOKEN è configurato nei secrets (Settings → Secrets)
2. Token non è scaduto o revoked
3. Nessun conflitto di versione su PyPI (impossibile overwrite)
4. Email PyPI account è verificata
```

### ❌ Tag non pubblica

```
Verifica:
1. Il tag esiste: git tag | grep vX.X.X
2. Il tag è pushato: git push origin vX.X.X
3. Il workflow è attivo (non disabilitato)
4. Actions è abilitato nel repo
```

---

## 🚀 Manual Publishing (Emergency)

Se il workflow fallisce, pubblica manualmente:

```bash
# Build
uv build packages/viaggiatreno
uv build packages/viaggiatreno_mcp

# Pubblica (richiede PYPI_TOKEN env var)
export PYPI_TOKEN=pypi-...
uv publish --token "$PYPI_TOKEN"
```

---

## 📝 Checklist Pre-Release

- [ ] Tutti i test passano (`pytest tests/`)
- [ ] Lint passa (`ruff check packages/`)
- [ ] Type check passa (`pyright packages/`)
- [ ] README.md aggiornato
- [ ] CHANGELOG aggiornato (opzionale)
- [ ] Versione in `packages/viaggiatreno/src/viaggiatreno/__init__.py` (version string, se presente)
- [ ] Versione coerente in entrambi i `pyproject.toml`
- [ ] Commit pushato a main
- [ ] Tag creato e pushato

---

## 🎯 Workflow Finale

```
1. Make changes
   ↓
2. Run tests locally: pytest tests/
   ↓
3. Commit & push to main
   ↓
4. Create tag: git tag v0.2.0
   ↓
5. Push tag: git push origin v0.2.0
   ↓
6. GitHub Actions automaticamente:
   - Build entrambi i pacchetti
   - Pubblica su PyPI
   - Crea GitHub Release
   ↓
7. Verifica su PyPI (2-5 minuti)
```

---

## 📚 Riferimenti

- [PyPI Documentation](https://packaging.python.org/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Semantic Versioning](https://semver.org/)
- [uv publish docs](https://docs.astral.sh/uv/reference/cli/#uv-publish)
