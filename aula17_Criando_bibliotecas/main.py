from aula17_Criando_bibliotecas.tonhuTwit import Twitter

consumer_key =	"WDsEyiugPHG6nSRAB3laRtoBD"
consumer_secret = "KIvJv65fGk03JVLeojRaeRUUZmK5nrSa76BIm60VmPK6uljqIy"
access_token = "321997268-4xy8FnAUobMLcnr7n67najLElYzB99P4tGK9DQhv"
access_token_secret = "sgs1ha6AOOopBpZ5FB4dWg35PV97j7OcjXJ6ne1mam4Ef"

twitter = Twitter(consumer_key, consumer_secret, access_token, access_token_secret)

twitter.menu()
