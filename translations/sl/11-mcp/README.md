<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T09:12:38+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "sl"
}
-->
# Lekcija 11: Integracija protokola Model Context Protocol (MCP)

## Uvod v protokol Model Context Protocol (MCP)

Protokol Model Context Protocol (MCP) je napreden okvir, zasnovan za standardizacijo interakcij med AI modeli in odjemalskimi aplikacijami. MCP deluje kot most med AI modeli in aplikacijami, ki jih uporabljajo, ter zagotavlja enoten vmesnik ne glede na implementacijo modela.

Ključni vidiki MCP:

- **Standardizirana komunikacija**: MCP vzpostavlja skupen jezik za komunikacijo med aplikacijami in AI modeli
- **Izboljšano upravljanje konteksta**: Omogoča učinkovito posredovanje kontekstualnih informacij AI modelom
- **Medplatformska združljivost**: Deluje v različnih programskih jezikih, vključno s C#, Java, JavaScript, Python in TypeScript
- **Enostavna integracija**: Razvijalcem omogoča preprosto vključevanje različnih AI modelov v njihove aplikacije

MCP je še posebej uporaben pri razvoju AI agentov, saj omogoča agentom interakcijo z različnimi sistemi in viri podatkov prek enotnega protokola, kar jih naredi bolj prilagodljive in zmogljive.

## Cilji učenja
- Razumeti, kaj je MCP in kakšna je njegova vloga pri razvoju AI agentov
- Nastaviti in konfigurirati MCP strežnik za integracijo z GitHubom
- Zgraditi sistem z več agenti z uporabo orodij MCP
- Implementirati RAG (Retrieval Augmented Generation) z Azure Cognitive Search

## Predpogoji
- Python 3.8+
- Node.js 14+
- Azure naročnina
- GitHub račun
- Osnovno razumevanje Semantic Kernel

## Navodila za nastavitev

1. **Nastavitev okolja**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfiguracija Azure storitev**
   - Ustvarite vir Azure Cognitive Search
   - Nastavite Azure OpenAI storitev
   - Konfigurirajte okoljske spremenljivke v `.env`

3. **Nastavitev MCP strežnika**
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

## Osrednje komponente

### 1. Sistem z več agenti
- GitHub agent: Analiza repozitorijev
- Hackathon agent: Priporočila za projekte
- Events agent: Predlogi za tehnične dogodke

### 2. Integracija z Azure
- Cognitive Search za indeksiranje dogodkov
- Azure OpenAI za inteligenco agentov
- Implementacija vzorca RAG

### 3. Orodja MCP
- Analiza GitHub repozitorijev
- Pregled kode
- Ekstrakcija metapodatkov

## Pregled kode

Primer prikazuje:
1. Integracijo MCP strežnika
2. Orkestracijo več agentov
3. Integracijo z Azure Cognitive Search
4. Implementacijo vzorca RAG

Ključne funkcionalnosti:
- Analiza GitHub repozitorijev v realnem času
- Inteligentna priporočila za projekte
- Ujemanje dogodkov z uporabo Azure Search
- Pretakanje odgovorov z Chainlit

## Zagon primera

Za podrobna navodila za nastavitev in več informacij si oglejte [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Zaženite MCP strežnik:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Zaženite aplikacijo:
   ```bash
   chainlit run app.py -w
   ```

3. Preizkusite integracijo:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Odpravljanje težav

Pogoste težave in rešitve:
1. Težave s povezavo MCP
   - Preverite, ali strežnik deluje
   - Preverite razpoložljivost vrat
   - Potrdite GitHub žetone

2. Težave z Azure Search
   - Preverite povezovalne nize
   - Preverite obstoj indeksa
   - Potrdite nalaganje dokumentov

## Naslednji koraki
- Raziskovanje dodatnih orodij MCP
- Implementacija prilagojenih agentov
- Izboljšanje zmogljivosti RAG
- Dodajanje več virov dogodkov
- **Napredno**: Oglejte si [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) za primere komunikacije med agenti

## Viri
- [MCP za začetnike](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Dokumentacija Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Vodiči za Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo strokovno človeško prevajanje. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.