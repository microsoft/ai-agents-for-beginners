<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-05-21T09:34:22+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "pt"
}
-->
# Aula 11: Integração do Protocolo de Contexto do Modelo (MCP)

## Introdução ao Protocolo de Contexto do Modelo (MCP)

O Protocolo de Contexto do Modelo (MCP) é uma estrutura avançada criada para padronizar as interações entre modelos de IA e aplicações clientes. O MCP funciona como uma ponte entre os modelos de IA e as aplicações que os utilizam, oferecendo uma interface consistente independentemente da implementação do modelo subjacente.

Aspectos principais do MCP:

- **Comunicação Padronizada**: O MCP estabelece uma linguagem comum para que as aplicações se comuniquem com os modelos de IA
- **Gerenciamento Aprimorado de Contexto**: Permite a passagem eficiente de informações contextuais para os modelos de IA
- **Compatibilidade Multiplataforma**: Funciona com várias linguagens de programação, incluindo C#, Java, JavaScript, Python e TypeScript
- **Integração Sem Esforço**: Permite que desenvolvedores integrem facilmente diferentes modelos de IA em suas aplicações

O MCP é especialmente valioso no desenvolvimento de agentes de IA, pois possibilita que agentes interajam com diversos sistemas e fontes de dados por meio de um protocolo unificado, tornando-os mais flexíveis e poderosos.

## Objetivos de Aprendizagem
- Compreender o que é o MCP e seu papel no desenvolvimento de agentes de IA
- Configurar e ajustar um servidor MCP para integração com GitHub
- Construir um sistema multiagente usando as ferramentas MCP
- Implementar RAG (Retrieval Augmented Generation) com Azure Cognitive Search

## Pré-requisitos
- Python 3.8+
- Node.js 14+
- Assinatura Azure
- Conta GitHub
- Conhecimento básico de Semantic Kernel

## Instruções de Configuração

1. **Configuração do Ambiente**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configurar Serviços Azure**
   - Crie um recurso Azure Cognitive Search
   - Configure o serviço Azure OpenAI
   - Ajuste as variáveis de ambiente no arquivo `.env`

3. **Configuração do Servidor MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Estrutura do Projeto

```
11-mcp/
├── code_samples/
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## Componentes Principais

### 1. Sistema Multiagente
- GitHub Agent: Análise de repositórios
- Hackathon Agent: Recomendações de projetos
- Events Agent: Sugestões de eventos tecnológicos

### 2. Integração com Azure
- Cognitive Search para indexação de eventos
- Azure OpenAI para inteligência dos agentes
- Implementação do padrão RAG

### 3. Ferramentas MCP
- Análise de repositórios GitHub
- Inspeção de código
- Extração de metadados

## Análise do Código

O exemplo demonstra:
1. Integração do servidor MCP
2. Orquestração multiagente
3. Integração com Azure Cognitive Search
4. Implementação do padrão RAG

Principais funcionalidades:
- Análise em tempo real de repositórios GitHub
- Recomendações inteligentes de projetos
- Correspondência de eventos usando Azure Search
- Respostas em streaming com Chainlit

## Executando o Exemplo

Para instruções detalhadas de configuração e mais informações, consulte o [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Inicie o servidor MCP:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Inicie a aplicação:
   ```bash
   chainlit run app.py -w
   ```

3. Teste a integração:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Solução de Problemas

Problemas comuns e soluções:
1. Problemas de Conexão MCP
   - Verifique se o servidor está rodando
   - Confira a disponibilidade da porta
   - Confirme os tokens do GitHub

2. Problemas com Azure Search
   - Valide as strings de conexão
   - Verifique a existência do índice
   - Confirme o upload dos documentos

## Próximos Passos
- Explore ferramentas MCP adicionais
- Implemente agentes personalizados
- Aprimore as capacidades do RAG
- Adicione mais fontes de eventos

## Recursos
- [MCP para Iniciantes](https://aka.ms/mcp-for-beginners)  
- [Documentação MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Documentação Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Guias Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.