<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:37:37+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "sw"
}
-->
# Somo la 11: Ujumuishaji wa Model Context Protocol (MCP)

## Utangulizi wa Model Context Protocol (MCP)

Model Context Protocol (MCP) ni mfumo wa kisasa uliobuniwa kusawazisha mawasiliano kati ya mifano ya AI na programu za wateja. MCP hufanya kazi kama daraja kati ya mifano ya AI na programu zinazotumia mifano hiyo, ikitoa kiolesura thabiti bila kujali utekelezaji wa mfano wa msingi.

Vipengele muhimu vya MCP:

- **Mawasiliano Yaliyosawazishwa**: MCP huanzisha lugha ya kawaida kwa programu kuwasiliana na mifano ya AI  
- **Usimamizi wa Muktadha Ulioboreshwa**: Huwezesha upitishaji wa taarifa za muktadha kwa ufanisi kwa mifano ya AI  
- **Utangamano wa Mifumo Mbalimbali**: Hufanya kazi katika lugha mbalimbali za programu kama C#, Java, JavaScript, Python, na TypeScript  
- **Ujumuishaji Usio na Shida**: Huwaruhusu watengenezaji kuunganisha kwa urahisi mifano tofauti ya AI kwenye programu zao  

MCP ni muhimu sana katika maendeleo ya mawakala wa AI kwa kuwa inaruhusu mawakala kuingiliana na mifumo na vyanzo vya data mbalimbali kupitia itifaki moja, na kuwafanya mawakala kuwa rahisi na wenye nguvu zaidi.

## Malengo ya Kujifunza
- Kuelewa MCP ni nini na jukumu lake katika maendeleo ya mawakala wa AI  
- Kusakinisha na kusanidi seva ya MCP kwa ujumuishaji wa GitHub  
- Kujenga mfumo wa mawakala wengi kwa kutumia zana za MCP  
- Kutekeleza RAG (Retrieval Augmented Generation) kwa Azure Cognitive Search  

## Mahitaji ya Awali
- Python 3.8+  
- Node.js 14+  
- Akaunti ya Azure  
- Akaunti ya GitHub  
- Uelewa wa msingi wa Semantic Kernel  

## Maelekezo ya Usanidi

1. **Usanidi wa Mazingira**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Sanidi Huduma za Azure**  
   - Unda rasilimali ya Azure Cognitive Search  
   - Sanidi huduma ya Azure OpenAI  
   - Sanidi vigezo vya mazingira kwenye `.env`  

3. **Usanidi wa Seva ya MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Muundo wa Mradi

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

## Vipengele Muhimu

### 1. Mfumo wa Mawakala Wengi  
- Wakala wa GitHub: Uchambuzi wa hazina  
- Wakala wa Hackathon: Mapendekezo ya miradi  
- Wakala wa Matukio: Mapendekezo ya matukio ya kiteknolojia  

### 2. Ujumuishaji wa Azure  
- Cognitive Search kwa kuorodhesha matukio  
- Azure OpenAI kwa akili ya mawakala  
- Utekelezaji wa muundo wa RAG  

### 3. Zana za MCP  
- Uchambuzi wa hazina za GitHub  
- Ukaguzi wa msimbo  
- Uchimbaji wa metadata  

## Uhakiki wa Msimbo

Mfano unaonyesha:  
1. Ujumuishaji wa seva ya MCP  
2. Uratibu wa mawakala wengi  
3. Ujumuishaji wa Azure Cognitive Search  
4. Utekelezaji wa muundo wa RAG  

Vipengele muhimu:  
- Uchambuzi wa hazina za GitHub kwa wakati halisi  
- Mapendekezo ya miradi yenye akili  
- Ulinganishaji wa matukio kwa kutumia Azure Search  
- Majibu ya mtiririko kwa kutumia Chainlit  

## Kuendesha Mfano

Kwa maelekezo ya kina ya usanidi na maelezo zaidi, rejelea [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Anzisha seva ya MCP:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Zindua programu:  
   ```bash
   chainlit run app.py -w
   ```

3. Jaribu ujumuishaji:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Utatuzi wa Shida

Masuala ya kawaida na suluhisho:  
1. Masuala ya Muunganisho wa MCP  
   - Hakikisha seva inaendesha  
   - Angalia upatikanaji wa bandari  
   - Thibitisha tokeni za GitHub  

2. Masuala ya Azure Search  
   - Thibitisha nyuzi za muunganisho  
   - Angalia uwepo wa faharasa  
   - Hakikisha nyaraka zimepakiwa  

## Hatua Zifuatazo
- Chunguza zana za ziada za MCP  
- Tekeleza mawakala maalum  
- Boresha uwezo wa RAG  
- Ongeza vyanzo zaidi vya matukio  
- **Juu Zaidi**: Angalia [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) kwa mifano ya mawasiliano kati ya mawakala  

## Rasilimali
- [MCP kwa Anayeanza](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)  
- [Mwongozo wa Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)  

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.