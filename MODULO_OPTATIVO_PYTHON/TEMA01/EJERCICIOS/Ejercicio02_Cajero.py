class Cajero:
    def __init__(self):
        self.monto = 50000
        print('BIENVENIDO A SU CAJERO AUTOMATICO')
        
    def operaciones(self):
        self.opcion = int(input('''
        ------------------------------------------------
        POR FAVOR INDIQUE QUE OPERACION DESEA REALIZAR..
        ------------------------------------------------
        1. CONSULTAR BALANCE
        2. DEPOSITO A CUENTA
        3. RETIRO DE EFECTIVO
        4. SALIR
        '''))
        self.control=0
        while self.control==0:
            if self.opcion==1:
                self.consultabalance()
            elif self.opcion==2:
                self.depositar()
            elif self.opcion==3:
                self.retirar()
            elif self.opcion==4:
                self.salir()
                self.control=1
            else:
                print('LO SENTIMOS OPCION NO VALIDA!, INTENTE DE NUEVO.. ')
                self.operaciones()

    def consultabalance(self):
        print('SU BALANCE DISPONIBLE ES: ', self.monto)
        print('DESEA REALIZAR OTRA OPERACION?')
        self.operaciones()

    def depositar(self):
        self.deposito = int(input('INDIQUE LA CANTIDAD A DEPOSITAR.. '))
        self.monto=self.monto + self.deposito
        self.consultabalance()

    def retirar(self):
        self.retiro = int(input('INDIQUE LA CANTIDAD A RETIRAR.. '))
        self.control = 0
        while self.control==0:
            if self.retiro > self.monto:
                print('''USTED NO POSEE FONDOS SUFICIENTES PARA ESTE RETIRO
                POR FAVOR INTENTE DE NUEVO..
                --------------------------------------------''')
                self.retiro = int(input('INDIQUE LA CANTIDAD A RETIRAR.. '))
            elif self.retiro<= self.monto:
                self.monto=self.monto-self.retiro
                print('CANTIDAD RETIRADA: ', self.retiro)
                self.consultabalance()
                self.control=1

    def salir(self):
        print('=======================================')
        print('GRACIAS POR USAR NUESTROS SERVICIOS!')
        print('=======================================')

ejecucion = Cajero()
ejecucion.operaciones()