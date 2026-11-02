---
name: testing-course-samples
---
# Testando os Exemplos do Curso

Valide que os notebooks das lições e os exemplos de código funcionam em uma configuração ativa
Microsoft Foundry / Azure OpenAI. O repositório inclui um executor em
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) que
executa todos os notebooks Python de forma headless e imprime uma matriz PASS/FAIL.

## Quando usar
- "Validar todos os notebooks / exemplos contra minha assinatura Azure."
- "Teste rápido do curso após atualizar pacotes ou mudar modelos."
- "Quais lições ainda funcionam / falham ao vivo?"

Não use isso para o GitHub Action AI Smoke Test (que valida agentes *implantados*
hospedados — veja [`tests/README.md`](../../../tests/README.md)). Esta habilidade
executa os notebooks localmente.

## Pré-requisitos (verifique primeiro)
1. **Python 3.12+** com dependências do curso: `python -m pip install -r requirements.txt`
   mais o executor: `python -m pip install nbconvert ipykernel`.
2. **`.env` na raiz do repositório** (copie de [`.env.example`](../../../../../.env.example)) com pelo menos:
   - `AZURE_AI_PROJECT_ENDPOINT` — endpoint do projeto Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — um deployment não depreciado (ex: `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) e `AZURE_OPENAI_DEPLOYMENT`
     para lições que chamam Azure OpenAI diretamente (Lição 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** concluído — exemplos se autenticam com `AzureCliCredential` (Entra ID, sem chave).
4. Verifique se o deployment do modelo existe:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Executando a validação
```powershell
# Todos os notebooks Python (ignora .NET, .venv, site-packages, traduções, recursos de habilidades)
pwsh scripts/validate-notebooks.ps1

# Uma única lição, com um tempo limite por célula mais longo
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Apenas lista o que seria executado (sem execução)
pwsh scripts/validate-notebooks.ps1 -List

# Interpretador explícito (se `python` não estiver no PATH, por exemplo, alias da Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
O script grava cópias executadas, logs por notebook e `results.json` em
`$env:TEMP\aiab-nbval` e finaliza com o número de falhas.

Falhas transitórias (limites HTTP 429 em assinaturas compartilhadas, um eventual
problema no token `AzureCliCredential` ou um timeout) são automaticamente
tentadas novamente (`-Retries`, padrão 2, com `-RetryDelaySeconds` de espera, padrão 20). Se um
deployment de modelo estiver gerando 429s regularmente, verifique a cota TPM GlobalStandard da assinatura
(`az cognitiveservices usage list -l <region>`) — aumentar a capacidade de um único
deployment não ajuda quando a cota da *assinatura* está esgotada.

## Interpretando resultados
- `PASS` — o notebook rodou de ponta a ponta sem erro em células.
- `FAIL` — a primeira linha `*Error` / `*Exception` é exibida; abra o
  `log_*.txt` correspondente na pasta de saída para o traceback completo.
- A falha de um único notebook é limitada por `-Timeout` (por célula), então uma célula
  de intervenção humana travada aparece como `StdinNotImplementedError` ao invés de travar.

## Lições que precisam de recursos extras (espera-se que falhem sem eles)
| Lição | Requisito extra |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, chave) — possui caminho de fallback em memória |
| 11 MCP / GitHub | Servidor MCP GitHub + PAT |
| 13 memória (cognee) | `cognee` configurado com um provedor de modelo |
| 15 uso no navegador | Navegadores Playwright instalados (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 agente local | Runtime local Foundry + modelo Qwen baixado (no dispositivo, sem nuvem) |
| notebooks `*-dotnet-*` | kernel .NET Interactive (excluído por padrão; use `-IncludeDotnet`) |

## Reportando resultados
Resuma em uma tabela PASS/FAIL agrupada por lição. Separe regressões genuínas
(bugs de código/configuração a corrigir) de lacunas de ambiente (Search/Foundry Local/PAT ausentes),
e cite o `log_*.txt` falho para cada falha real.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->