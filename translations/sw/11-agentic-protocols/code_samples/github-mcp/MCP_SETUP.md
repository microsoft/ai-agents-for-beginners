<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T21:27:08+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "sw"
}
-->
# Mwongozo wa Ujumuishaji wa MCP Server

## Mahitaji ya Awali
- Node.js imewekwa (toleo la 14 au zaidi)
- Meneja wa kifurushi cha npm
- Mazingira ya Python yenye utegemezi unaohitajika

## Hatua za Kuseti

1. **Sakinisha Kifurushi cha MCP Server**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Anzisha MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Server inapaswa kuanza na kuonyesha URL ya muunganisho.

3. **Hakikisha Muunganisho**
   - Tafuta ikoni ya plagi (🔌) kwenye kiolesura cha Chainlit  
   - Nambari (1) inapaswa kuonekana karibu na ikoni ya plagi ikionyesha muunganisho umefanikiwa  
   - Console inapaswa kuonyesha: "GitHub plugin setup completed successfully" (pamoja na mistari ya hali ya ziada)

## Utatuzi wa Shida

### Masuala ya Kawaida

1. **Mzozo wa Bandari**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Suluhisho: Badilisha bandari kwa kutumia:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Masuala ya Uthibitishaji**
   - Hakikisha sifa za GitHub zimewekwa vizuri  
   - Angalia faili ya .env ina tokeni zinazohitajika  
   - Thibitisha ufikiaji wa API ya GitHub  

3. **Muunganisho Umeshindwa**
   - Hakikisha server inaendesha kwenye bandari inayotarajiwa  
   - Angalia mipangilio ya firewall  
   - Thibitisha mazingira ya Python yana vifurushi vinavyohitajika  

## Uthibitishaji wa Muunganisho

Server yako ya MCP imeunganishwa vizuri ikiwa:  
1. Console inaonyesha "GitHub plugin setup completed successfully"  
2. Magogo ya muunganisho yanaonyesha "✓ MCP Connection Status: Active"  
3. Amri za GitHub zinafanya kazi kwenye kiolesura cha mazungumzo  

## Vigezo vya Mazingira

Vinavyohitajika kwenye faili yako ya .env:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Kupima Muunganisho

Tuma ujumbe huu wa majaribio kwenye mazungumzo:  
```
Show me the repositories for username: [GitHub Username]
```  
Jibu lenye mafanikio litaonyesha taarifa za hifadhi.  

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutokuelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.