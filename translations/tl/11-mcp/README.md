<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T08:51:48+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "tl"
}
-->
# Aralin 11: Pagsasama ng Model Context Protocol (MCP)

## Panimula sa Model Context Protocol (MCP)

Ang Model Context Protocol (MCP) ay isang makabagong balangkas na idinisenyo upang gawing pamantayan ang interaksyon sa pagitan ng mga AI model at mga kliyenteng aplikasyon. Ang MCP ay nagsisilbing tulay sa pagitan ng mga AI model at mga aplikasyon na gumagamit nito, na nagbibigay ng pare-parehong interface anuman ang implementasyon ng model.

Mahahalagang aspeto ng MCP:

- **Pamantayang Komunikasyon**: Ang MCP ay nagtatatag ng isang karaniwang wika para makipag-usap ang mga aplikasyon sa mga AI model  
- **Pinahusay na Pamamahala ng Konteksto**: Nagpapahintulot ng mahusay na pagpapasa ng impormasyong kontekstwal sa mga AI model  
- **Pagkakatugma sa Iba't Ibang Plataporma**: Gumagana sa iba't ibang programming language tulad ng C#, Java, JavaScript, Python, at TypeScript  
- **Madaling Pagsasama**: Pinapadali ang integrasyon ng iba't ibang AI model sa mga aplikasyon  

Ang MCP ay partikular na mahalaga sa pagbuo ng mga AI agent dahil pinapayagan nito ang mga agent na makipag-ugnayan sa iba't ibang sistema at pinagkukunan ng datos sa pamamagitan ng isang pinag-isang protocol, na ginagawang mas flexible at makapangyarihan ang mga agent.

## Mga Layunin sa Pagkatuto
- Maunawaan kung ano ang MCP at ang papel nito sa pagbuo ng mga AI agent  
- I-set up at i-configure ang isang MCP server para sa integrasyon sa GitHub  
- Bumuo ng isang multi-agent system gamit ang mga MCP tool  
- Ipatupad ang RAG (Retrieval Augmented Generation) gamit ang Azure Cognitive Search  

## Mga Kinakailangan
- Python 3.8+  
- Node.js 14+  
- Azure subscription  
- GitHub account  
- Pangunahing kaalaman sa Semantic Kernel  

## Mga Tagubilin sa Setup

1. **Pag-set up ng Kapaligiran**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **I-configure ang mga Azure Service**  
   - Gumawa ng Azure Cognitive Search resource  
   - I-set up ang Azure OpenAI service  
   - I-configure ang mga environment variable sa `.env`  

3. **Setup ng MCP Server**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Estruktura ng Proyekto

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

## Mga Pangunahing Komponent

### 1. Multi-Agent System
- GitHub Agent: Pagsusuri ng repository  
- Hackathon Agent: Mga rekomendasyon sa proyekto  
- Events Agent: Mga suhestiyon sa tech na kaganapan  

### 2. Integrasyon sa Azure
- Cognitive Search para sa pag-index ng mga kaganapan  
- Azure OpenAI para sa katalinuhan ng agent  
- Pagpapatupad ng RAG pattern  

### 3. Mga MCP Tool
- Pagsusuri ng repository sa GitHub  
- Pag-inspeksyon ng code  
- Pagkuha ng metadata  

## Paglalakad sa Code

Ipinapakita ng halimbawa ang:  
1. Integrasyon ng MCP server  
2. Orkestrasyon ng multi-agent  
3. Integrasyon sa Azure Cognitive Search  
4. Pagpapatupad ng RAG pattern  

Mga pangunahing tampok:  
- Real-time na pagsusuri ng repository sa GitHub  
- Matalinong rekomendasyon sa proyekto  
- Pagtutugma ng kaganapan gamit ang Azure Search  
- Streaming na mga tugon gamit ang Chainlit  

## Pagpapatakbo ng Halimbawa

Para sa detalyadong mga tagubilin sa setup at karagdagang impormasyon, tingnan ang [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Simulan ang MCP server:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Ilunsad ang aplikasyon:  
   ```bash
   chainlit run app.py -w
   ```

3. Subukan ang integrasyon:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Pag-aayos ng Problema

Mga karaniwang isyu at solusyon:  
1. Mga Isyu sa Koneksyon ng MCP  
   - Siguraduhing tumatakbo ang server  
   - Suriin ang availability ng port  
   - Kumpirmahin ang mga token ng GitHub  

2. Mga Isyu sa Azure Search  
   - I-validate ang mga connection string  
   - Suriin ang pagkakaroon ng index  
   - Kumpirmahin ang pag-upload ng dokumento  

## Mga Susunod na Hakbang
- Tuklasin ang karagdagang mga MCP tool  
- Magpatupad ng mga custom na agent  
- Pagandahin ang mga kakayahan ng RAG  
- Magdagdag ng mas maraming pinagkukunan ng kaganapan  
- **Advanced**: Tingnan ang [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) para sa mga halimbawa ng komunikasyon sa pagitan ng mga agent  

## Mga Mapagkukunan
- [MCP para sa mga Baguhan](https://aka.ms/mcp-for-beginners)  
- [Dokumentasyon ng MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Mga Dokumento ng Azure Cognitive Search](https://learn.microsoft.com/azure/search/)  
- [Mga Gabay sa Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)  

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.