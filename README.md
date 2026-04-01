# script_COADv1
Script inicial que auxilia na busca de dados específicos dentro dos documentos em formato .html mirando na base de dados inicial da COAD/ICMBio. A ferramenta tem o foco em fazer com que o trabalho primário de cadastro de informações seja feito totalmente pelo script mais rápido e em menos tempo.

Fluxo Principal:
 - O programa começa processando um a um os documentos da pasta direcionada, no momento apenas em formato .html;
 - Ele busca os campos que foram pré definos em código dentro de cada tag html, se não encontra ele não retorna nenhum dado. (foi a forma de buscar os dados de forma mais precisa, evitando erros de preenchimento que ocorreriam com mais frequência em buscas sem um escopo bem definido dentro do código do documento);
 - Após a análise é retornado um documento .xlxs para uso no excel.

Futuras Melhorias:
 - Resolução de casos específicos dos documentos que não foram processados ou reconhecimentos;
 - Interface de interação com o usuário;
 - Banco de dados mais bem estruturado fazendo com que o uso de planilhas não seja o meio principal de disceminação de dados.