<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:46:27+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "hr"
}
-->
# Lekcija 11: Integracija Model Context Protocol (MCP)

## Uvod u Model Context Protocol (MCP)

Model Context Protocol (MCP) je napredni okvir osmišljen za standardizaciju interakcija između AI modela i klijentskih aplikacija. MCP služi kao most između AI modela i aplikacija koje ih koriste, pružajući dosljedno sučelje bez obzira na implementaciju modela u pozadini.

Ključni aspekti MCP-a:

- **Standardizirana komunikacija**: MCP uspostavlja zajednički jezik za komunikaciju između aplikacija i AI modela
- **Poboljšano upravljanje kontekstom**: Omogućuje učinkovito prosljeđivanje kontekstualnih informacija AI modelima
- **Kompatibilnost između platformi**: Radi na različitim programskim jezicima, uključujući C#, Java, JavaScript, Python i TypeScript
- **Jednostavna integracija**: Omogućuje programerima jednostavnu integraciju različitih AI modela u njihove aplikacije

MCP je posebno koristan u razvoju AI agenata jer omogućuje agentima interakciju s različitim sustavima i izvorima podataka putem jedinstvenog protokola, čineći agente fleksibilnijima i moćnijima.

## Ciljevi učenja
- Razumjeti što je MCP i njegovu ulogu u razvoju AI agenata
- Postaviti i konfigurirati MCP poslužitelj za integraciju s GitHubom
- Izgraditi sustav s više agenata koristeći MCP alate
- Implementirati RAG (Retrieval Augmented Generation) s Azure Cognitive Search

## Preduvjeti
- Python 3.8+
- Node.js 14+
- Azure pretplata
- GitHub račun
- Osnovno razumijevanje Semantic Kernel-a

## Upute za postavljanje

1. **Postavljanje okruženja**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfiguracija Azure usluga**
   - Kreirajte resurs za Azure Cognitive Search
   - Postavite Azure OpenAI uslugu
   - Konfigurirajte varijable okruženja u `.env`

3. **Postavljanje MCP poslužitelja**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Struktura projekta

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## Ključne komponente

### 1. Sustav s više agenata
- GitHub agent: Analiza repozitorija
- Hackathon agent: Preporuke za projekte
- Events agent: Prijedlozi za tehnološke događaje

### 2. Integracija s Azureom
- Cognitive Search za indeksiranje događaja
- Azure OpenAI za inteligenciju agenata
- Implementacija RAG uzorka

### 3. MCP alati
- Analiza GitHub repozitorija
- Pregled koda
- Ekstrakcija metapodataka

## Pregled koda

Primjer demonstrira:
1. Integraciju MCP poslužitelja
2. Orkestraciju više agenata
3. Integraciju s Azure Cognitive Search
4. Implementaciju RAG uzorka

Ključne značajke:
- Analiza GitHub repozitorija u stvarnom vremenu
- Inteligentne preporuke za projekte
- Podudaranje događaja pomoću Azure Search
- Streaming odgovora uz Chainlit

## Pokretanje primjera

Za detaljne upute o postavljanju i više informacija, pogledajte [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Pokrenite MCP poslužitelj:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Pokrenite aplikaciju:
   ```bash
   chainlit run app.py -w
   ```

3. Testirajte integraciju:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Rješavanje problema

Uobičajeni problemi i rješenja:
1. Problemi s MCP vezom
   - Provjerite radi li poslužitelj
   - Provjerite dostupnost porta
   - Potvrdite GitHub tokene

2. Problemi s Azure Search
   - Provjerite ispravnost konekcijskih nizova
   - Provjerite postoji li indeks
   - Potvrdite prijenos dokumenata

## Sljedeći koraci
- Istražite dodatne MCP alate
- Implementirajte prilagođene agente
- Poboljšajte RAG mogućnosti
- Dodajte više izvora događaja
- **Napredno**: Pogledajte [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) za primjere komunikacije između agenata

## Resursi
- [MCP za početnike](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search dokumentacija](https://learn.microsoft.com/azure/search/)
- [Vodiči za Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.