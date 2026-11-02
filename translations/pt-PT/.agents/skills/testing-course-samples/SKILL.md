---
name: testing-course-samples
---
# Testar os Exemplos do Curso

Valide que os cadernos da lição e os exemplos de código funcionam numa configuração live 
Microsoft Foundry / Azure OpenAI. O repositório inclui um executor em 
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) que 
executa todos os cadernos Python sem interface e imprime uma matriz PASS/FAIL.

## Quando usar
- "Validar todos os cadernos / exemplos na minha subscrição Azure."
- "Fazer um teste rápido do curso após atualizar pacotes ou alterar modelos."
- "Quais lições ainda passam / falham em live?"

Não utilize isto para o AI Smoke Test GitHub Action (que valida agentes *implantados* 
hospedados — veja [`tests/README.md`](../../../tests/README.md)). Esta ferramenta 
executa os cadernos localmente.

## Pré-requisitos (verificar primeiro)
1. **Python 3.12+** com as dependências do curso: `python -m pip install -r requirements.txt`
   mais o executor: `python -m pip install nbconvert ipykernel`.
2. **`.env` na raiz do repositório** (copiar desde [`.env.example`](../../../../../.env.example)) com pelo menos:
   - `AZURE_AI_PROJECT_ENDPOINT` — endpoint do projeto Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — um deployment não descontinuado (ex: `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) e `AZURE_OPENAI_DEPLOYMENT`
     para lições que chamam o Azure OpenAI diretamente (Lição 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** concluído — os exemplos autenticam com `AzureCliCredential` (Entra ID, sem chave).
4. Verificar que o deployment do modelo existe:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Executar a validação
```powershell
# Todos os notebooks Python (exclui .NET, .venv, site-packages, traduções, recursos de competências)
pwsh scripts/validate-notebooks.ps1

# Uma única lição, com um limite de tempo mais longo por célula
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Apenas listar o que seria executado (sem execução)
pwsh scripts/validate-notebooks.ps1 -List

# Interpretador explícito (se `python` não estiver no PATH, por exemplo, alias da Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
O script grava cópias executadas, logs por caderno, e `results.json` em
`$env:TEMP\aiab-nbval` e termina com o número de falhas.

Falhas transitórias (limites HTTP 429 de taxa de uma subscrição partilhada, um ocasional
problema de token `AzureCliCredential` ou timeout) são automaticamente re-tentadas
(`-Retries`, padrão 2, com `-RetryDelaySeconds` em recuo, padrão 20). Se um
deployment de modelo regularmente gerar 429, verifique a quota TPM GlobalStandard
da subscrição (`az cognitiveservices usage list -l <region>`) — aumentar a capacidade de um
único deployment não ajuda quando a quota da *subscrição* está esgotada.

## Interpretar os resultados
- `PASS` — o caderno executou completamente sem erro em células.
- `FAIL` — mostra a primeira linha `*Error` / `*Exception`; abra o arquivo
  `log_*.txt` correspondente na pasta de output para o traceback completo.
- Uma falha de um único caderno é limitada por `-Timeout` (por célula), assim uma célula
  com interação humana bloqueada aparece como `StdinNotImplementedError` em vez de travar.

## Lições que precisam de recursos extra (espera-se que falhem sem eles)
| Lição | Requisito extra |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, chave) — tem um caminho alternativo em memória |
| 11 MCP / GitHub | Servidor GitHub MCP + PAT |
| 13 memória (cognee) | `cognee` configurado com um provedor de modelo |
| 15 uso de browser | Browsers Playwright instalados (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 agente local | Runtime Foundry Local + um modelo Qwen descarregado (no dispositivo, sem cloud) |
| Cadernos `*-dotnet-*` | Kernel .NET Interactive (excluído por padrão; usar `-IncludeDotnet`) |

## Reportar resultados
Resuma numa tabela PASS/FAIL agrupada por lição. Separe regressões genuínas
(bugs no código/configuração para corrigir) de falhas de ambiente (falta de Search/Foundry Local/PAT),
e aponte o `log_*.txt` falhado para cada falha real.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->