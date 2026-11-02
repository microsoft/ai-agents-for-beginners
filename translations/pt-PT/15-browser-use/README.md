# Construir Agentes de Utilização de Computador (CUA)

Os agentes de utilização de computador podem interagir com websites da mesma forma que uma pessoa faria: abrindo um navegador, inspecionando a página, e tomando a melhor ação seguinte com base no que veem. Nesta lição, vais construir um agente de automação de navegador que pesquisa no Airbnb, extrai dados estruturados dos anúncios e identifica a estadia mais barata em Estocolmo.

A lição combina Browser-Use para navegação guiada por IA, Playwright e Chrome DevTools Protocol (CDP) para controlo do navegador, Azure OpenAI para raciocínio com visão, e Pydantic para extração estruturada.

## Introdução

Esta lição cobrirá:

- Compreender quando agentes de utilização de computador são mais indicados que automação só por API
- Combinar Browser-Use com Playwright e CDP para gestão fiável do ciclo de vida do navegador
- Usar Azure OpenAI com visão e output estruturado em Pydantic para extrair dados de anúncios em páginas web dinâmicas
- Decidir quando usar um fluxo de trabalho de automação browser-first, actor-first ou híbrido

## Objetivos de Aprendizagem

Depois de completar esta lição, saberás como:

- Configurar Browser-Use com Azure OpenAI e Playwright
- Construir um fluxo de automação de navegador que navega num website real e lida com elementos de UI dinâmicos
- Extrair resultados tipados do conteúdo visível na página e transformá-los em lógica de negócio posterior
- Escolher entre padrões agent e actor consoante a previsibilidade da tarefa no navegador

## Exemplo de Código

Esta lição inclui um tutorial em notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Lança uma sessão Chrome via CDP, pesquisa anúncios no Airbnb para Estocolmo, extrai preços com Browser-Use visão, e devolve a opção mais barata como dados estruturados.

## Requisitos

- Python 3.12+
- Desdobramento do Azure OpenAI configurado no teu ambiente
- Chrome ou Chromium instalado localmente
- Dependências do Playwright instaladas
- Familiaridade básica com Python assíncrono

## Configuração

Instala os pacotes usados no notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Define as variáveis de ambiente do Azure OpenAI usadas pelo notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opcional: predefinido para a versão mais recente da API quando omitido
AZURE_OPENAI_API_VERSION=...
```

## Visão Geral da Arquitetura

O notebook demonstra um fluxo de automação de navegador híbrido:

1. O Chrome arranca com CDP ativado para que tanto o Playwright como o Browser-Use possam partilhar a mesma sessão do navegador.
2. Um agente Browser-Use lida com tarefas de navegação abertas, como abrir o Airbnb, rejeitar pop-ups, e pesquisar Estocolmo.
3. A página ativa é inspecionada com um esquema estruturado Pydantic para extrair títulos de anúncios, preços por noite, avaliações e URLs.
4. A lógica em Python compara os anúncios extraídos e destaca o resultado mais barato.

Esta abordagem mantém o raciocínio flexível baseado em visão, em que o Browser-Use é bom, enquanto ainda oferece controlo determinístico do navegador quando necessário.

## Pilares Principais e Boas Práticas

### Quando Usar Agent vs Actor

| Cenário | Usar Agent | Usar Actor |
|---------|------------|-----------|
| Layouts dinâmicos | Sim, IA adapta-se a mudanças da página | Não, seletores frágeis podem quebrar |
| Estrutura conhecida | Não, agente é mais lento que controlo direto | Sim, rápido e preciso |
| Encontrar elementos | Sim, linguagem natural funciona bem | Não, selecionadores exatos são necessários |
| Controlo de tempo | Não, menos previsível | Sim, controlo total de esperas e tentativas |
| Fluxos de trabalho complexos | Sim, lida com estados inesperados da UI | Não, requer ramificações explícitas |

### Boas Práticas Browser-Use

1. Começa com um agente para exploração e navegação dinâmica.
2. Passa para controlo direto da página quando a interação se tornar previsível.
3. Usa modelos de output estruturados para que os dados extraídos sejam validados e com tipos seguros.
4. Adiciona atrasos estrategicamente após ações que desencadeiam mudanças visíveis na UI.
5. Captura capturas de ecrã enquanto itera para facilitar a depuração de erros.
6. Espera que websites mudem e desenha estratégias de fallback para pop-ups e alterações no layout.
7. Mistura os padrões agent e actor para obter flexibilidade e precisão.

### Salvaguardas de Segurança para Agentes de Navegador

Agentes de navegador operam em websites ao vivo, por isso precisam de limites mais apertados do que um script que apenas chama uma API conhecida. Antes de passar de uma demonstração em notebook para um fluxo real, define os controlos sobre o que o agente pode ver, clicar e submeter.

1. **Define o escopo do ambiente de navegação.** Executa o agente num perfil de navegador dedicado ou sandbox, limitando-o aos domínios necessários para a tarefa.
2. **Separa observação de ação.** Permite que o agente pesquise, leia e extraia dados primeiro; requer um passo explícito de aprovação antes de submeter formulários, enviar mensagens, marcar viagens, fazer compras, apagar registos ou alterar definições de conta.
3. **Mantém segredos fora dos prompts e registos.** Não coloques palavras-passe, dados de pagamento, cookies de sessão ou dados pessoais crus no contexto do modelo. Deixa que o utilizador tome conta da autenticação e revele campos sensíveis dos registos.
4. **Trata o conteúdo da página como input não confiável.** Um website pode conter instruções destinadas ao agente, não ao utilizador. O agente deve ignorar texto da página que lhe peça para mudar o objetivo, revelar dados, desativar salvaguardas ou visitar sites não relacionados.
5. **Usa verificações determinísticas em passos de risco.** Verifica a URL atual, título da página, item selecionado, preço, destinatário, e resumo da ação com código antes de pedir ao utilizador para aprovar o passo final.
6. **Define orçamentos e condições de paragem.** Limita o número de ações, tentativas, abas e minutos que o agente pode usar. Para quando o estado da página for ambíguo em vez de continuar a clicar.
7. **Regista evidência útil, não tudo.** Mantém resumos de ação, carimbos temporais, URLs, descrições de elementos selecionados, referências a capturas de ecrã para que as falhas possam ser revistas sem armazenar conteúdo sensível desnecessário da página.

No exemplo do Airbnb, o padrão seguro é pesquisar anúncios e extrair preços. Iniciar sessão, contactar um anfitrião ou completar uma reserva deve ser uma ação separada aprovada pelo utilizador.

### Aplicações no Mundo Real

- Reservas de viagem e monitorização de preços
- Comparação de preços e verificação de disponibilidade em e-commerce
- Extração estruturada de websites dinâmicos
- Testes e verificação de UI conscientes de visão
- Monitorização e alertas de websites
- Preenchimento inteligente de formulários em fluxos multi-etapa

## Exemplo no Mundo Real: Microsoft Project Opal

O agente que construíste nesta lição é uma versão pequena e local de um **agente de utilização de computador (CUA)** — um programa que conduz um navegador como uma pessoa faria. A Microsoft está a trazer esta mesma ideia para a empresa com o **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, uma capacidade no Microsoft 365 Copilot.

Com o Project Opal, descreves uma tarefa e o agente trabalha em teu nome usando **utilização de computador num Windows 365 Cloud PC seguro**, operando em toda a organização nas aplicações baseadas em navegador, sites e dados. Funciona **assincronamente em segundo plano**, e podes guiar o trabalho ou tomar controlo a qualquer momento. Exemplos de tarefas incluem:

- Gerir pedidos de associação a grupos de segurança
- Recolher e validar evidência de auditoria para revisões de conformidade
- Tratar incidentes de IT (atualizar estado de tickets, atribuir responsáveis, fechar duplicados)
- Compilar dados de Excel num relatório financeiro de fecho

O Opal é uma referência útil para o que um agente de utilização de computador **a nível de produção, confiável** deve parecer — e reforça conceitos de lições anteriores:

| Conceito neste curso | Como o Project Opal o aplica |
|----------------------|-----------------------------|
| **Humano no circuito** (Lição 06) | O Opal faz pausa para credenciais de login, dados sensíveis ou instruções ambíguas, e nunca introduz palavras-passe ou submete formulários sem confirmação explícita. Podes *Tomar Controlo* e *Devolver Controlo* durante a tarefa. |
| **Agentes confiáveis e seguros** (Lições 06 & 18) | Corre num Windows 365 Cloud PC isolado, é só navegador por padrão (outro acesso ao computador é bloqueado, aplicado via Intune), usa *a tua* identidade para aceder apenas ao que estás autorizado, e regista todas as ações para auditabilidade. |
| **Planificação e metacognição** (Lições 07 & 09) | O Opal gera primeiro um plano para a tarefa, depois supervisiona o seu próprio raciocínio a cada passo e faz pausa se detetar atividade suspeita. |
| **Capacidades / ferramentas reutilizáveis** (Lição 04) | **Skills** deixam-te escrever instruções para tarefas repetíveis (importadas de um ficheiro `.md` ou criadas com o Opal) e reusar em várias conversas. |

> **Disponibilidade:** O Project Opal está atualmente disponível para utilizadores no [programa de acesso antecipado Frontier](https://adoption.microsoft.com/copilot/frontier-program/) com uma subscrição Microsoft 365 Copilot, e o teu administrador deve completar a configuração. Por ser uma funcionalidade experimental Frontier, as capacidades podem mudar com o tempo.

## Verificação de Conhecimentos

Testa a tua compreensão antes de avançar para a próxima lição.

**1. Quando é que um agente de utilização de computador baseado em navegador é mais adequado que um fluxo só por API?**

<details>
<summary>Resposta</summary>

Usa um agente de navegador quando a tarefa depende do que é visível numa UI web, o site não expõe a API necessária, ou a página muda frequentemente o suficiente para que a lógica fixa da API ou dos seletores seja frágil. Se existir uma API estável para a mesma tarefa, prefere a API porque geralmente é mais rápida, fácil de testar e mais segura.
</details>

**2. Num fluxo híbrido, que partes deve o agente tratar e que partes deve o código direto do Playwright tratar?**

<details>
<summary>Resposta</summary>

Deixa o agente tratar da navegação aberta e estados dinâmicos da UI, como encontrar a página certa ou rejeitar pop-ups inesperados. Passa para controlo direto do Playwright quando a estrutura da página é conhecida e a ação precisa de precisão, tentativas, esperas ou validação determinística.
</details>

**3. O exemplo do Airbnb encontra um anúncio que o utilizador pode querer reservar. O que deve acontecer antes do fluxo iniciar sessão, contactar um anfitrião ou completar a reserva?**

<details>
<summary>Resposta</summary>

O fluxo deve fazer pausa e pedir aprovação explícita do utilizador. Antes de pedir, deve mostrar um resumo claro do anúncio selecionado, URL atual, preço, datas e ação pretendida. Pesquisar e extrair preços pode ser autónomo; o acesso à conta, mensagens, compras e reservas devem ser aprovados pelo utilizador.
</details>

**4. Uma página web diz ao agente para ignorar as instruções originais, visitar outro site e revelar credenciais guardadas. Como deve o agente tratar esse texto?**

<details>
<summary>Resposta</summary>

Trata-o como conteúdo da página não confiável, não como instrução de desenvolvedor ou utilizador. O agente deve manter-se dentro do domínio e escopo da tarefa autorizados, recusar revelar segredos, e evitar seguir texto da página que mude o objetivo, desative salvaguardas ou envie-o para sites não relacionados.
</details>

**5. Que evidência é útil guardar quando um agente de navegador está a correr, e o que deve ser evitado?**

<details>
<summary>Resposta</summary>

Guarda resumos de ações, carimbos de tempo, URLs, descrições dos elementos selecionados, resultados de validação e referências a capturas de ecrã para que a execução possa ser revista. Evita armazenar palavras-passe, dados de pagamento, cookies de sessão, dados pessoais crus, ou conteúdos completos da página a menos que haja uma razão específica de retenção e privacidade.
</details>

## Recursos Adicionais

- [Começar com o Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Template de integração Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parâmetros actor e extração de conteúdo Browser-Use](https://docs.browser-use.com/customize/actor/all-parameters)
- [Configuração do Curso](../00-course-setup/README.md)

## Lição Anterior

[Explorando Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Próxima Lição

[Desdobrar Agentes Escaláveis](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->