import stevedore

exts = stevedore.ExtensionManager(namespace='exampleclient.example')

fun1 = exts['sayhello']
fun1()
