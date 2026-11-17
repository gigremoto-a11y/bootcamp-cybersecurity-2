# 🛡️ Análise Conceitual e Mitigação de Ransomware e Keyloggers

Repositório desenvolvido como parte do desafio prático do **Bootcamp de Cibersegurança**. O objetivo deste projeto é explorar os fundamentos técnicos de duas das ameaças mais comuns no cenário de segurança da informação atual, **Ransomware** e **Keylogger**, compreendendo seus mecanismos de funcionamento para projetar estratégias eficazes de **detecção, mitigação e defesa**.

---

## 📂 Estrutura do Repositório

- `README.md`: Documentação técnica, análise de riscos e guia de defesas.
- `demos/`: Demonstrações conceituais em ambiente isolado focadas no entendimento de bibliotecas e APIs (sem caráter ofensivo ou exfiltração).
  - `crypto_demo.py`: Uso básico de criptografia simétrica para proteção de dados em repouso.
  - `keylogger_demo.py`: Monitoramento local de eventos de teclado para fins de auditoria de acessibilidade/entrada.

---

## 🔍 1. Ransomware: Análise Conceitual

O ransomware é um tipo de malware que restringe o acesso ao sistema ou a arquivos específicos do usuário e cobra um valor de resgate ("ransom") para restaurar o acesso.

### Como funciona (Visão Geral):
1. **Infiltração:** Geralmente ocorre via engenharia social (phishing), exploração de vulnerabilidades não corrigidas (patches desatualizados) ou credenciais comprometidas (RDP exposto).
2. **Descoberta e Enumeração:** O malware varre o sistema de arquivos local e unidades de rede mapeadas em busca de extensões específicas (documentos, planilhas, bancos de dados).
3. **Criptografia:** Utiliza algoritmos robustos (como AES-256 combinados com RSA-4096 para proteção de chaves) para embaralhar os dados das vítimas.
4. **Extorsão:** O acesso às chaves privadas de descriptografia é retido pelo atacante, muitas vezes acompanhado por ameaças de vazamento de dados (dupla extorsão).

### Mecanismos de Defesa e Mitigação:
- **Estratégia de Backups 3-2-1:** Manter 3 cópias dos dados, em 2 mídias diferentes, sendo pelo menos 1 cópia **offline/imutável** (air-gapped). Esta é a principal linha de defesa contra ransomware.
- **Princípio do Menor Privilégio (PoLP):** Restringir permissões de escrita de usuários e processos em diretórios críticos do sistema e compartilhamentos de rede.
- **Detecção Comportamental (EDR):** Ferramentas modernas de Endpoint Detection and Response monitoram padrões anômalos de I/O (ex: alteração em massa rápida de extensões e arquivos).
- **Segmentação de Rede:** Impedir o movimento lateral do malware para outros servidores e estações de trabalho.

---

## ⌨️ 2. Keylogger: Análise Conceitual

Um keylogger é um software ou hardware projetado para monitorar e registrar cada tecla pressionada em um teclado, geralmente de forma oculta, com o objetivo de capturar credenciais, senhas e informações confidenciais.

### Como funciona (Visão Geral):
1. **Hooking do Sistema Operacional:** O software intercepta eventos de hardware ou chamadas de API do sistema operacional (como o subsistema de janelas ou hooks de teclado) para escutar o fluxo de entrada (`input streams`).
2. **Armazenamento Local:** Os caracteres capturados são salvos temporariamente em arquivos de log locais ou buffers de memória.
3. **Exfiltração de Dados:** Em cenários maliciosos, esses dados são enviados periodicamente para um servidor de comando e controle (C2) por meio de canais criptografados (HTTPS, DNS tunneling) ou protocolos como SMTP.

### Mecanismos de Defesa e Mitigação:
- **Autenticação Multifator (MFA):** Mitiga drasticamente o impacto de credenciais comprometidas por keyloggers, pois a senha capturada sozinha se torna insuficiente para o acesso.
- **Teclados Virtuais e On-Screen Keyboards:** Úteis em terminais públicos ou ambientes altamente sensíveis para evitar captura baseada em interceptação direta de hardware/software padrão.
- **Controle de Aplicativos e Whitelisting:** Impedir a execução de binários não autorizados que tentem registrar hooks globais no sistema operacional.
- **Soluções Antivírus e Anti-Spyware:** Assinaturas e análises heurísticas capazes de identificar chamadas suspeitas de APIs de monitoramento de periféricos.

---

## 🛡️ 3. Conclusão e Governança de Segurança

A simulação e o estudo analítico de malwares reforçam que a segurança da informação não depende de uma única ferramenta milagrosa, mas sim de uma **abordagem em camadas (Defense in Depth)**. 

A mitigação eficaz exige a combinação de:
- **Tecnologia:** Atualizações constantes, EDRs, backups imutáveis e firewalls robustos.
- **Processos:** Políticas de acesso restrito e resposta a incidentes bem ensaiada.
- **Pessoas:** Conscientização contínua dos colaboradores por meio de treinamentos anti-phishing, já que o fator humano continua sendo o vetor inicial mais explorado.
