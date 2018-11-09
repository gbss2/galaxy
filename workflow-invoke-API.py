from bioblend import galaxy

#SETTINGS
#url de acesso a instancia do GCloud onde o Galaxy esta hospedado
instance_url = 'http://35.224.111.104'
#chave para acesso a instance de Galaxy via API
API_key = '2b16b35c558c591d712b8e988ddb4a57'
#arquivos de input
r1_reads = '/local/path/to/file_r1'
r2_reads = '/local/path/to/file_r2'

#cria um objeto da instancia Galaxy
gi = galaxy.GalaxyInstance(url=instance_url, key=API_key)

#sobe os arquivos de input para a biblioteca com id=1cd8e2f6b131e891 (test-large-files)
#gi.libraries.upload_file_from_local_path(library_id='1cd8e2f6b131e891', file_local_path='/local/path/to/file_r1')
#gi.libraries.upload_file_from_local_path(library_id='1cd8e2f6b131e891', file_local_path='/local/path/to/file_r2')

#roda o workflow de id=1cd8e2f6b131e891 (Trimming and Quality Control)
#as etapas 0 e 1 sao "Input Dataset" e representam input respectivamente das reads R1 e R2
gi.workflows.invoke_workflow(workflow_id='1cd8e2f6b131e891', inputs={'0':{'id': '84f63edc852e8a15', 'src': 'hda'}, '1':{'id': '02290d3eb960301f', 'src': 'hda'}})
