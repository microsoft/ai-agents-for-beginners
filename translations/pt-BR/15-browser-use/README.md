# Construindo Agentes de Uso de Computador (CUA)

Agentes de uso de computador podem interagir com websites do mesmo jeito que uma pessoa faria: abrindo um navegador, inspecionando a página e tomando a melhor decisão a partir do que veem. Nesta lição, você construirá um agente de automação de navegador que busca no Airbnb, extrai dados estruturados de anúncios e identifica a estadia mais barata em Estocolmo.

A lição combina Browser-Use para navegação dirigida por IA, Playwright e Chrome DevTools Protocol (CDP) para controle do navegador, Azure OpenAI para raciocínio habilitado por visão, e Pydantic para extração estruturada.

## Introdução

Esta lição abordará:

- Entender quando agentes de uso de computador são mais indicados do que automação apenas via API
- Combinar Browser-Use com Playwright e CDP para gerenciamento confiável do ciclo de vida do navegador
- Usar visão Azure OpenAI e saída estruturada Pydantic para extrair dados de anúncios de páginas web dinâmicas
- Decidir quando usar um fluxo de automação de navegador com agente primeiro, ator primeiro, ou híbrido

## Objetivos de Aprendizagem

Após completar esta lição, você saberá como:

- Configurar Browser-Use com Azure OpenAI e Playwright
- Construir um fluxo de automação de navegador que navega em um site real e lida com elementos dinâmicos da interface
- Extrair resultados tipados do conteúdo visível da página e transformá-los em lógica de negócios downstream
- Escolher entre padrões de agente e ator com base na previsibilidade da tarefa do navegador

## Exemplo de Código

Esta lição inclui um tutorial em notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Inicia uma sessão Chrome via CDP, pesquisa anúncios do Airbnb em Estocolmo, extrai preços com visão Browser-Use, e retorna a opção mais barata como dados estruturados.

## Pré-requisitos

- Python 3.12+
- Implantação Azure OpenAI configurada no seu ambiente
- Chrome ou Chromium instalado localmente
- Dependências do Playwright instaladas
- Familiaridade básica com Python assíncrono

## Configuração

Instale os pacotes usados no notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Defina as variáveis de ambiente Azure OpenAI usadas pelo notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opcional: padrão para a versão mais recente da API quando omitido
AZURE_OPENAI_API_VERSION=...
```

## Visão Geral da Arquitetura

O notebook demonstra um fluxo híbrido de automação de navegador:

1. O Chrome inicia com CDP habilitado para que Playwright e Browser-Use possam compartilhar a mesma sessão do navegador.
2. Um agente Browser-Use gerencia tarefas de navegação abertas como abrir o Airbnb, dispensar pop-ups e pesquisar Estocolmo.
3. A página ativa é inspecionada com um esquema estruturado Pydantic para extrair títulos dos anúncios, preços por noite, avaliações e URLs.
4. A lógica Python compara os anúncios extraídos e destaca o resultado mais barato.

Essa abordagem mantém o raciocínio flexível baseado em visão que Browser-Use faz bem, enquanto te dá controle determinístico do navegador quando necessário.

## Pontos-Chave e Boas Práticas

### Quando Usar Agente vs Ator

| Cenário | Usar Agente | Usar Ator |
|----------|-----------|-----------|
| Layouts dinâmicos | Sim, IA pode se adaptar a mudanças na página | Não, seletores frágeis podem quebrar |
| Estrutura conhecida | Não, agente é mais lento que controle direto | Sim, rápido e preciso |
| Encontrar elementos | Sim, linguagem natural funciona bem | Não, seletores exatos são necessários |
| Controle de tempo | Não, menos previsível | Sim, controle total sobre esperas e tentativas |
| Fluxos complexos | Sim, lida com estados inesperados da UI | Não, requer ramificações explícitas |

### Boas Práticas de Browser-Use

1. Comece com um agente para exploração e navegação dinâmica.
2. Mude para controle direto da página quando a interação se tornar previsível.
3. Use modelos de saída estruturada para que os dados extraídos sejam validados e tipados com segurança.
4. Adicione atrasos estrategicamente após ações que provocam mudanças visíveis na UI.
5. Capture screenshots enquanto itera para facilitar debugging de falhas.
6. Espere que sites mudem e desenhe estratégias de fallback para pop-ups e deslocamentos de layout.
7. Misture padrões de agente e ator para obter flexibilidade e precisão.

### Medidas de Segurança para Agentes de Navegador

Agentes de navegador operam em sites ao vivo, então precisam de limites mais rigorosos que um script que só chama uma API conhecida. Antes de sair de um demo em notebook para um fluxo real, defina controles sobre o que o agente pode ver, clicar e enviar.

1. **Limite o ambiente de navegação.** Rode o agente em um perfil de navegador ou sandbox dedicado, e restrinja aos domínios necessários para a tarefa.
2. **Separe observação de ação.** Deixe o agente buscar, ler e extrair dados primeiro; exija aprovação explícita antes de enviar formulários, enviar mensagens, reservar viagens, realizar compras, apagar registros ou alterar configurações.
3. **Mantenha segredos fora de prompts e rastros.** Não coloque senhas, detalhes de pagamento, cookies de sessão ou dados pessoais crus no contexto do modelo. Deixe o usuário assumir a autenticação e redigir campos sensíveis dos logs.
4. **Trate conteúdo da página como entrada não confiável.** Um site pode conter instruções destinadas ao agente, não ao usuário. O agente deve ignorar textos que peçam para mudar suas metas, revelar dados, desativar salvaguardas ou visitar sites não relacionados.
5. **Use verificações determinísticas em passos arriscados.** Verifique URL atual, título da página, item selecionado, preço, destinatário e resumo da ação com código antes de pedir aprovação final do usuário.
6. **Defina orçamentos e condições de parada.** Limite o número de ações, tentativas, abas e minutos que o agente pode usar. Pare quando o estado da página estiver ambíguo em vez de continuar clicando.
7. **Registre evidências úteis, não tudo.** Mantenha resumos das ações, timestamps, URLs, descrições dos elementos selecionados e referências a screenshots para que falhas possam ser revisadas sem armazenar conteúdo sensível desnecessário.

No exemplo do Airbnb, o padrão seguro é buscar anúncios e extrair preços. Fazer login, contactar um anfitrião ou concluir uma reserva deve ser uma ação separada aprovada pelo usuário.

### Aplicações no Mundo Real

- Reserva de viagens e monitoramento de preços
- Comparação de preços e checagem de disponibilidade em e-commerce
- Extração estruturada de sites dinâmicos
- Teste e verificação de UI com suporte de visão
- Monitoramento e alerta de sites
- Preenchimento inteligente de formulários em fluxos multi-etapas

## Exemplo Real: Microsoft Project Opal

O agente que você constrói nesta lição é uma versão pequena e local de um **agente de uso de computador (CUA)** — um programa que dirige um navegador da mesma forma que uma pessoa. A Microsoft está levando essa mesma ideia para a empresa com o **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, uma funcionalidade do Microsoft 365 Copilot.

Com o Project Opal, você descreve uma tarefa e o agente trabalha em seu nome usando **uso do computador em um Windows 365 Cloud PC seguro**, operando entre os aplicativos, sites e dados baseados em navegador da sua organização. Funciona **assincronamente em segundo plano**, e você pode guiar o trabalho ou assumir o controle a qualquer momento. Exemplos de tarefas incluem:

- Gerenciar solicitações de associação a grupos de segurança
- Coletar e validar evidências de auditoria para revisões de conformidade
- Triar incidentes de TI (atualizar status de tickets, atribuir responsáveis, fechar duplicados)
- Compilar dados do Excel em um deck de fechamento financeiro

Opal é uma referência útil para como é um agente de uso de computador **de nível de produção e confiável** — e reforça conceitos de lições anteriores:

| Conceito neste curso | Como o Project Opal aplica |
|------------------------|-----------------------------|
| **Humano no loop** (Lição 06) | Opal pausa para credenciais de login, dados sensíveis ou instruções ambíguas, e nunca insere senhas nem envia formulários sem confirmação explícita. Você pode *Assumir Controle* e *Devolver Controle* no meio da tarefa. |
| **Agentes seguros e confiáveis** (Lições 06 & 18) | Roda em um Windows 365 Cloud PC isolado, é somente navegador por padrão (outro acesso ao computador bloqueado via Intune), usa *sua* identidade para acessar só o autorizado, e registra cada ação para auditoria. |
| **Planejamento & metacognição** (Lições 07 & 09) | Opal gera um plano da tarefa primeiro, depois supervisiona seu próprio raciocínio em cada passo e pausa se detectar atividade suspeita. |
| **Capacidades / ferramentas reutilizáveis** (Lição 04) | **Skills** deixam você escrever instruções para trabalhos repetíveis (importadas de arquivo `.md` ou criadas com Opal) e reutilizá-las em conversas. |

> **Disponibilidade:** O Project Opal está atualmente disponível para usuários no [programa de acesso antecipado Frontier](https://adoption.microsoft.com/copilot/frontier-program/) com assinatura Microsoft 365 Copilot, e seu administrador deve completar a configuração. Por ser um recurso experimental Frontier, as capacidades podem mudar com o tempo.

## Recursos Adicionais

- [Comece com o Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Template de integração Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parâmetros de ator e extração de conteúdo Browser-Use](https://docs.browser-use.com/customize/actor/all-parameters)
- [Configuração do Curso](../00-course-setup/README.md)

## Lição Anterior

[Explorando o Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Próxima Lição

[Desenvolvendo Agentes Escaláveis](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->