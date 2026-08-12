# Construir Agentes de Utilização de Computador (CUA)

Os agentes de utilização de computador podem interagir com websites da mesma forma que uma pessoa: abrindo um navegador, inspecionando a página e tomando a melhor ação seguinte com base no que veem. Nesta lição, irá construir um agente de automação do navegador que pesquisa no Airbnb, extrai dados estruturados das listagens e identifica a estadia mais barata em Estocolmo.

A lição combina Browser-Use para navegação orientada por IA, Playwright e Chrome DevTools Protocol (CDP) para controlo do navegador, Azure OpenAI para raciocínio habilitado por visão e Pydantic para extração estruturada.

## Introdução

Esta lição cobrirá:

- Compreender quando os agentes de utilização de computador são mais adequados do que a automação apenas via API
- Combinar Browser-Use com Playwright e CDP para uma gestão fiável do ciclo de vida do navegador
- Utilizar visão Azure OpenAI e saída estruturada Pydantic para extrair dados de listagem de páginas web dinâmicas
- Decidir quando usar um fluxo de trabalho de automação de navegador centrado em agente, ator, ou híbrido

## Objetivos de Aprendizagem

Após completar esta lição, saberá como:

- Configurar o Browser-Use com Azure OpenAI e Playwright
- Construir um fluxo de automação de navegador que navegue num website real e lide com elementos UI dinâmicos
- Extrair resultados tipados a partir do conteúdo visível da página e transformá-los em lógica de negócio downstream
- Escolher entre padrões de agente e ator com base na previsibilidade da tarefa no navegador

## Exemplo de Código

Esta lição inclui um tutorial em notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Lança uma sessão Chrome por CDP, pesquisa listagens no Airbnb para Estocolmo, extrai preços com visão Browser-Use, e retorna a opção mais barata como dados estruturados.

## Pré-requisitos

- Python 3.12+
- Implementação Azure OpenAI configurada no seu ambiente
- Chrome ou Chromium instalado localmente
- Dependências Playwright instaladas
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
# Opcional: assume por defeito a versão mais recente da API quando omitido
AZURE_OPENAI_API_VERSION=...
```

## Visão Geral da Arquitetura

O notebook demonstra um fluxo de automação de navegador híbrido:

1. O Chrome inicia com CDP ativado para que tanto o Playwright quanto o Browser-Use possam partilhar a mesma sessão do navegador.
2. Um agente Browser-Use gere tarefas de navegação abertas, como abrir o Airbnb, dispensar pop-ups e pesquisar Estocolmo.
3. A página ativa é inspecionada com um esquema Pydantic estruturado para extrair títulos das listagens, preços por noite, avaliações e URLs.
4. A lógica Python compara as listagens extraídas e destaca a opção mais barata.

Esta abordagem mantém o raciocínio flexível e baseado em visão pelo qual o Browser-Use é bom, enquanto ainda oferece controlo determinístico do navegador quando necessário.

## Principais Aprendizagens e Boas Práticas

### Quando Usar Agente vs Ator

| Cenário | Usar Agente | Usar Ator |
|----------|-----------|-----------|
| Layouts dinâmicos | Sim, IA pode adaptar-se a mudanças na página | Não, seletores frágeis podem quebrar |
| Estrutura conhecida | Não, um agente é mais lento que controlo direto | Sim, rápido e preciso |
| Encontrar elementos | Sim, linguagem natural funciona bem | Não, são necessários seletores exatos |
| Controlo de temporização | Não, menos previsível | Sim, controlo total sobre esperas e re-tentativas |
| Fluxos de trabalho complexos | Sim, lida com estados UI inesperados | Não, requer ramificação explícita |

### Boas Práticas Browser-Use

1. Comece com um agente para exploração e navegação dinâmica.
2. Mude para controlo direto da página quando a interação se tornar previsível.
3. Use modelos de saída estruturada para que dados extraídos sejam validados e sejam seguros em termos de tipo.
4. Adicione atrasos estrategicamente após ações que desencadeiem alterações visíveis na UI.
5. Capture capturas de ecrã enquanto itera para facilitar a depuração de falhas.
6. Espere que websites mudem e desenhe estratégias de fallback para pop-ups e alterações de layout.
7. Misture padrões de agente e ator para obter flexibilidade e precisão.

### Guardrails de Segurança para Agentes de Navegador

Agentes de navegador operam em websites ao vivo, portanto necessitam de limites mais apertados do que um script que apenas chama uma API conhecida. Antes de passar de uma demo em notebook para um fluxo de trabalho real, defina os controlos sobre o que o agente pode ver, clicar e submeter.

1. **Delimite o ambiente de navegação.** Execute o agente num perfil dedicado do navegador ou sandbox, e limite-o aos domínios necessários para a tarefa.
2. **Separe observação de ação.** Deixe o agente pesquisar, ler e extrair dados primeiro; exija uma etapa explícita de aprovação antes que envie formulários, envie mensagens, faça reservas, compre, elimine registos ou altere definições de conta.
3. **Mantenha segredos fora dos prompts e rastos.** Não coloque palavras-passe, detalhes de pagamento, cookies de sessão ou dados pessoais crus no contexto do modelo. Deixe o utilizador assumir para autenticação e redigir campos sensíveis dos registos.
4. **Trate o conteúdo da página como uma entrada não confiável.** Um website pode conter instruções destinadas ao agente, não ao utilizador. O agente deve ignorar texto na página que lhe peça para mudar o objetivo, revelar dados, desativar salvaguardas ou visitar sites não relacionados.
5. **Use verificações determinísticas em passos arriscados.** Verifique a URL atual, título da página, item selecionado, preço, destinatário e sumário de ação com código antes de pedir ao utilizador para aprovar o passo final.
6. **Defina limites e condições de paragem.** Limite o número de ações, re-tentativas, separadores e minutos que o agente pode usar. Pare quando o estado da página for ambíguo em vez de continuar a clicar.
7. **Registe evidências úteis, não tudo.** Guarde sumários de ação, carimbos temporais, URLs, descrições dos elementos selecionados e referências de capturas de ecrã para que falhas possam ser revistas sem armazenar conteúdo sensível desnecessário.

No exemplo Airbnb, o padrão seguro é pesquisar listagens e extrair preços. Fazer login, contactar um anfitrião ou concluir uma reserva deve ser uma ação separada aprovada pelo utilizador.

### Aplicações no Mundo Real

- Reserva de viagens e monitorização de preços
- Comparação de preços de comércio eletrónico e verificações de disponibilidade
- Extração estruturada de websites dinâmicos
- Testes e verificação UI com visão computacional
- Monitorização e alerta de websites
- Preenchimento inteligente de formulários em fluxos multi-etapas

## Exemplo Real: Microsoft Project Opal

O agente que constrói nesta lição é uma pequena versão local de um **agente de utilização de computador (CUA)** — um programa que conduz um navegador como uma pessoa faria. A Microsoft está a trazer esta mesma ideia para as empresas com o **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, uma funcionalidade do Microsoft 365 Copilot.

Com o Project Opal, descreve uma tarefa e o agente trabalha em seu nome usando **utilização de computador num PC Cloud Windows 365 seguro**, operando entre as aplicações, sites e dados baseados no navegador da sua organização. Funciona **assíncronamente em segundo plano**, e pode orientar o trabalho ou assumir controlo a qualquer momento. Exemplos de tarefas incluem:

- Gerir pedidos de pertença a grupos de segurança
- Recolher e validar evidências de auditoria para revisões de conformidade
- Triagem de incidentes de IT (atualizar estado de tickets, atribuir responsáveis, fechar duplicados)
- Compilar dados Excel num deck de fecho financeiro

O Opal é uma referência útil para o aspeto de um agente de utilização de computador **fiável e preparado para produção** — e reforça conceitos de lições anteriores:

| Conceito neste curso | Como o Project Opal o aplica |
|------------------------|-----------------------------|
| **Human-in-the-loop** (Lição 06) | O Opal para para credenciais de login, dados sensíveis ou instruções ambíguas, e nunca introduz palavras-passe ou envia formulários sem confirmação explícita. Pode *Assumir Controlo* e *Devolver Controlo* a meio da tarefa. |
| **Agentes fiáveis e seguros** (Lições 06 & 18) | Corre num PC Cloud Windows 365 isolado, é apenas navegador por padrão (outro acesso de computador bloqueado, aplicado via Intune), usa *a sua* identidade para só aceder ao que tem autorização, e regista cada ação para auditabilidade. |
| **Planeamento & metacognição** (Lições 07 & 09) | O Opal gera primeiro um plano para a tarefa, depois supervisiona o seu próprio raciocínio em cada passo e para se detetar atividade suspeita. |
| **Capacidades / ferramentas reutilizáveis** (Lição 04) | As **Competências** permitem escrever instruções para trabalhos repetíveis (importadas de um ficheiro `.md` ou criadas com Opal) e reutilizá-las em conversas. |

> **Disponibilidade:** O Project Opal está atualmente disponível para utilizadores no [programa de acesso antecipado Frontier](https://adoption.microsoft.com/copilot/frontier-program/) com uma subscrição Microsoft 365 Copilot, e o seu administrador deve completar a configuração. Por ser uma funcionalidade experimental Frontier, as capacidades podem mudar ao longo do tempo.

## Recursos Adicionais

- [Começar com o Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Template de integração Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parâmetros de ator Browser-Use e extração de conteúdo](https://docs.browser-use.com/customize/actor/all-parameters)
- [Configuração do Curso](../00-course-setup/README.md)

## Lição Anterior

[Explorando o Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Próxima Lição

[Desplegar Agentes Escaláveis](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->