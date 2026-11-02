# Construindo Agentes de Uso de Computador (CUA)

Agentes de uso de computador podem interagir com sites da mesma forma que uma pessoa: abrindo um navegador, inspecionando a página e tomando a próxima melhor ação a partir do que veem. Nesta lição, você vai construir um agente de automação de navegador que pesquisa no Airbnb, extrai dados estruturados das listas e identifica a estadia mais barata em Estocolmo.

A lição combina Browser-Use para navegação guiada por IA, Playwright e o Protocolo Chrome DevTools (CDP) para controle do navegador, Azure OpenAI para raciocínio habilitado por visão, e Pydantic para extração estruturada.

## Introdução

Esta lição abordará:

- Compreender quando agentes de uso de computador são mais adequados que automação apenas por API
- Combinar Browser-Use com Playwright e CDP para gerenciamento confiável do ciclo de vida do navegador
- Usar visão do Azure OpenAI e saída estruturada com Pydantic para extrair dados de listagens em páginas web dinâmicas
- Decidir quando usar um fluxo de automação de navegador focado em agente, ator, ou híbrido

## Objetivos de Aprendizagem

Após completar esta lição, você saberá como:

- Configurar Browser-Use com Azure OpenAI e Playwright
- Construir um fluxo de automação de navegador que navega em um site real e manipula elementos dinâmicos da interface
- Extrair resultados tipados do conteúdo visível da página e transformá-los em lógica de negócio subsequente
- Escolher entre os padrões agente e ator com base em quão previsível é a tarefa no navegador

## Exemplo de Código

Esta lição inclui um tutorial em notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Inicia uma sessão do Chrome via CDP, pesquisa listagens em Estocolmo no Airbnb, extrai preços com a visão do Browser-Use e retorna a opção mais barata como dados estruturados.

## Pré-requisitos

- Python 3.12+
- Implantação do Azure OpenAI configurada em seu ambiente
- Chrome ou Chromium instalado localmente
- Dependências do Playwright instaladas
- Familiaridade básica com Python assíncrono

## Configuração

Instale os pacotes usados no notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Defina as variáveis de ambiente do Azure OpenAI usadas pelo notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opcional: padrão para a versão mais recente da API quando omitido
AZURE_OPENAI_API_VERSION=...
```

## Visão Geral da Arquitetura

O notebook demonstra um fluxo híbrido de automação de navegador:

1. O Chrome é iniciado com CDP habilitado para que Playwright e Browser-Use possam compartilhar a mesma sessão de navegador.
2. Um agente do Browser-Use manipula tarefas de navegação abertas, como abrir o Airbnb, dispensar pop-ups e pesquisar Estocolmo.
3. A página ativa é inspecionada com um esquema Pydantic estruturado para extrair títulos das listagens, preços por noite, avaliações e URLs.
4. A lógica em Python compara as listagens extraídas e destaca o resultado mais barato.

Essa abordagem mantém o raciocínio baseado em visão flexível que o Browser-Use faz bem, ao mesmo tempo que oferece controle determinístico do navegador quando necessário.

## Principais Conclusões e Boas Práticas

### Quando Usar Agente vs Ator

| Cenário | Usar Agente | Usar Ator |
|----------|-------------|-----------|
| Layouts dinâmicos | Sim, IA pode se adaptar a mudanças na página | Não, seletores frágeis podem quebrar |
| Estrutura conhecida | Não, um agente é mais lento que controle direto | Sim, rápido e preciso |
| Encontrar elementos | Sim, linguagem natural funciona bem | Não, seletores exatos são necessários |
| Controle de tempo | Não, menos previsível | Sim, controle total sobre esperas e tentativas |
| Fluxos complexos | Sim, lida com estados inesperados da UI | Não, requer ramificações explícitas |

### Boas Práticas com Browser-Use

1. Comece com um agente para exploração e navegação dinâmica.
2. Mude para controle direto da página quando a interação se tornar previsível.
3. Use modelos de saída estruturada para que os dados extraídos sejam validados e type-safe.
4. Adicione atrasos estrategicamente após ações que disparam mudanças visíveis na UI.
5. Capture capturas de tela durante a iteração para facilitar a depuração de falhas.
6. Espere que sites mudem e projete estratégias de contingência para pop-ups e mudanças no layout.
7. Misture padrões de agente e ator para obter tanto flexibilidade quanto precisão.

### Diretrizes de Segurança para Agentes de Navegador

Agentes de navegador operam em sites ao vivo, portanto precisam de limites mais rigorosos que um script que apenas chama uma API conhecida. Antes de avançar de um demo em notebook para um fluxo real, defina os controles sobre o que o agente pode ver, clicar e submeter.

1. **Delimite o ambiente de navegação.** Execute o agente em um perfil dedicado do navegador ou sandbox, e limite-o aos domínios necessários para a tarefa.
2. **Separe observação de ação.** Deixe o agente pesquisar, ler e extrair dados primeiro; exija uma etapa explícita de aprovação antes que ele envie formulários, envie mensagens, reserve viagens, faça compras, delete registros ou altere configurações de conta.
3. **Mantenha segredos fora de prompts e registros.** Não coloque senhas, detalhes de pagamento, cookies de sessão ou dados pessoais crus no contexto do modelo. Deixe o usuário assumir a autenticação e remova campos sensíveis dos logs.
4. **Trate o conteúdo da página como entrada não confiável.** Um site pode conter instruções destinadas ao agente, não ao usuário. O agente deve ignorar textos que peçam para mudar seu objetivo, revelar dados, desabilitar proteções ou visitar sites não relacionados.
5. **Use verificações determinísticas em etapas de risco.** Verifique a URL atual, título da página, item selecionado, preço, destinatário e resumo da ação com código antes de pedir aprovação do usuário para o passo final.
6. **Defina orçamentos e condições de parada.** Limite o número de ações, tentativas, abas e minutos que o agente pode usar. Pare quando o estado da página for ambíguo ao invés de continuar clicando.
7. **Registre evidências úteis, não tudo.** Guarde resumos de ações, timestamps, URLs, descrições dos elementos selecionados e referências de capturas de tela para que falhas possam ser revisadas sem armazenar conteúdo sensível desnecessário da página.

No exemplo do Airbnb, o padrão seguro é pesquisar listagens e extrair preços. Entrar na conta, contatar um anfitrião ou completar uma reserva deve ser uma ação separada aprovada pelo usuário.

### Aplicações no Mundo Real

- Reservas de viagem e monitoramento de preços
- Comparação de preços de e-commerce e verificação de disponibilidade
- Extração estruturada de sites dinâmicos
- Testes e verificação de UI com consciência visual
- Monitoramento e alertas de sites
- Preenchimento inteligente de formulários em fluxos multi-etapas

## Exemplo do Mundo Real: Microsoft Project Opal

O agente que você constrói nesta lição é uma pequena versão local de um **agente de uso de computador (CUA)** — um programa que conduz um navegador da maneira que uma pessoa faria. A Microsoft está trazendo essa mesma ideia para a empresa com **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, uma funcionalidade no Microsoft 365 Copilot.

Com o Project Opal, você descreve uma tarefa e o agente atua em seu nome usando **uso de computador em um Windows 365 Cloud PC seguro**, operando em aplicativos, sites e dados baseados em navegador da sua organização. Ele funciona **assíncronamente em segundo plano**, e você pode guiar o trabalho ou assumir o controle a qualquer momento. Exemplos de trabalhos incluem:

- Gerenciar solicitações de membros de grupo de segurança
- Coletar e validar evidências de auditoria para revisões de conformidade
- Triagem de incidentes de TI (atualizar status de tickets, atribuir responsáveis, fechar duplicatas)
- Compilar dados do Excel em um relatório de fechamento financeiro

Opal é uma referência útil para como um agente de uso de computador **de nível de produção e confiável** é — e reforça conceitos das lições anteriores:

| Conceito neste curso | Como o Project Opal aplica |
|----------------------|--------------------------|
| **Humano no loop** (Lição 06) | Opal pausa para credenciais de login, dados sensíveis ou instruções ambíguas, e nunca insere senhas ou submete formulários sem confirmação explícita. Você pode *Tomar Controle* e *Retornar Controle* no meio da tarefa. |
| **Agentes confiáveis e seguros** (Lições 06 & 18) | Roda em um Windows 365 Cloud PC isolado, é só navegador por padrão (acesso a outros computadores bloqueado, imposto via Intune), usa *sua* identidade para acessar somente o que está autorizado, e registra cada ação para auditoria. |
| **Planejamento & metacognição** (Lições 07 & 09) | Opal gera um plano para a tarefa primeiro, depois supervisiona seu próprio raciocínio em cada passo e pausa se detectar atividade suspeita. |
| **Capacidades / ferramentas reutilizáveis** (Lição 04) | **Skills** permitem que você escreva instruções para trabalhos repetíveis (importadas de um arquivo `.md` ou criadas com Opal) e reutilize-as em conversas. |

> **Disponibilidade:** O Project Opal está atualmente disponível para usuários no [programa de acesso antecipado Frontier](https://adoption.microsoft.com/copilot/frontier-program/) com uma assinatura do Microsoft 365 Copilot, e seu administrador deve concluir a configuração. Por ser um recurso experimental do Frontier, as capacidades podem mudar com o tempo.

## Verificação de Conhecimento

Teste sua compreensão antes de avançar para a próxima lição.

**1. Quando um agente de uso de computador baseado em navegador é mais adequado que um fluxo apenas por API?**

<details>
<summary>Resposta</summary>

Use um agente de navegador quando a tarefa depender do que é visível na interface web, o site não expõe a API necessária, ou a página muda com frequência suficiente para que uma lógica fixa de API ou seletores seja frágil. Se existir uma API estável para a mesma tarefa, prefira a API pois geralmente é mais rápida, fácil de testar e segura.
</details>

**2. Em um fluxo híbrido, quais partes o agente deve manipular e quais partes o código direto do Playwright deve manipular?**

<details>
<summary>Resposta</summary>

Deixe o agente lidar com navegação aberta e estados dinâmicos da UI, como encontrar a página certa ou dispensar pop-ups inesperados. Mude para controle direto do Playwright quando a estrutura da página for conhecida e a ação precisar de precisão, tentativas, esperas ou validação determinística.
</details>

**3. O exemplo do Airbnb encontra uma listagem que o usuário pode querer reservar. O que deve acontecer antes que o fluxo faça login, contacte um anfitrião ou complete a reserva?**

<details>
<summary>Resposta</summary>

O fluxo deve pausar e pedir aprovação explícita do usuário. Antes disso, deve mostrar um resumo claro da listagem selecionada, URL atual, preço, datas e ação pretendida. Pesquisar e extrair preços pode ser autônomo; acesso à conta, mensagens, compras e reservas devem ser aprovados pelo usuário.
</details>

**4. Uma página web diz ao agente para ignorar suas instruções originais, visitar outro site e revelar credenciais salvas. Como o agente deve tratar esse texto?**

<details>
<summary>Resposta</summary>

Trate isso como conteúdo da página não confiável, não como instrução do desenvolvedor ou usuário. O agente deve permanecer dentro do domínio e escopo da tarefa permitidos, recusar revelar segredos, e evitar seguir texto da página que altera o objetivo, desativa proteções ou o envia para sites não relacionados.
</details>

**5. Qual evidência é útil guardar quando um agente de navegador está em execução, e o que deve ser evitado?**

<details>
<summary>Resposta</summary>

Guarde resumos de ações, timestamps, URLs, descrições dos elementos selecionados, resultados de validação e referências de capturas de tela para que a execução possa ser revisada. Evite armazenar senhas, detalhes de pagamento, cookies de sessão, dados pessoais crus ou conteúdos completos da página a menos que haja um motivo específico de retenção e privacidade.
</details>

## Recursos Adicionais

- [Comece com o Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Template de integração do Browser-Use com Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parâmetros do ator Browser-Use e extração de conteúdo](https://docs.browser-use.com/customize/actor/all-parameters)
- [Configuração do curso](../00-course-setup/README.md)

## Lição Anterior

[Explorando o Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Próxima Lição

[Implementando Agentes Escaláveis](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->