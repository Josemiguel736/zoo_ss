from app.models import TipoEntrada,Entrada,TiketsGroup
import pytest
def test_create_ticket():
    ticket=Entrada(2)
    assert ticket.edad==2
    assert ticket.tipo==TipoEntrada.BEBE
    assert ticket.precio==0

    ticket=Entrada(12)
    assert ticket.edad==12
    assert ticket.tipo==TipoEntrada.NIÑO
    assert ticket.precio==14

    ticket=Entrada(26)
    assert ticket.edad==26
    assert ticket.tipo==TipoEntrada.ADULTO
    assert ticket.precio==23

    ticket=Entrada(66)
    assert ticket.edad==66
    assert ticket.tipo==TipoEntrada.JUBILADO
    assert ticket.precio==18


def test_create_negative_age_ticket():
    with pytest.raises(ValueError):
        entrada=Entrada(-2)
   


def test_create_tickets_group():
    group=TiketsGroup()
    assert group.total==0
    assert group.num_entradas==0

def test_add_tickets_group():
    group=TiketsGroup()
    group.add_ticket(24)
    assert group.total==23
    assert group.num_entradas==1
    group.add_ticket(13)
    assert group.total==37
    assert group.num_entradas==2
    group.add_ticket(65)
    assert group.total==55
    assert group.num_entradas==3
    group.add_ticket(2)
    assert group.total==55
    assert group.num_entradas==4

def test_count_tipe_entradas():
    group=TiketsGroup()
    group.add_ticket(32)
    assert group.count_type_tickets(TipoEntrada.ADULTO)==1
    group.add_ticket(4)
    assert group.count_type_tickets(TipoEntrada.ADULTO)==1
    assert group.count_type_tickets(TipoEntrada.NIÑO)==1
    group.add_ticket(5)
    group.add_ticket(66)
    assert group.count_type_tickets(TipoEntrada.ADULTO)==1
    assert group.count_type_tickets(TipoEntrada.NIÑO)==2
    assert group.count_type_tickets(TipoEntrada.JUBILADO)==1
    group.add_ticket(0)
    assert group.count_type_tickets(TipoEntrada.ADULTO)==1
    assert group.count_type_tickets(TipoEntrada.NIÑO)==2
    assert group.count_type_tickets(TipoEntrada.JUBILADO)==1
    assert group.count_type_tickets(TipoEntrada.BEBE)==1

def test_subtotal_of_type():
    group=TiketsGroup()
    group.add_ticket(12)
    assert group.subtotal_for_type(TipoEntrada.NIÑO)==14
    group.add_ticket(12)
    assert group.subtotal_for_type(TipoEntrada.NIÑO)==28
    group.add_ticket(2)
    group.add_ticket(22)
    assert group.subtotal_for_type(TipoEntrada.NIÑO)==28
    assert group.subtotal_for_type(TipoEntrada.ADULTO)==23
    assert group.subtotal_for_type(TipoEntrada.BEBE)==0
    group.add_ticket(22)
    assert group.subtotal_for_type(TipoEntrada.NIÑO)==28
    assert group.subtotal_for_type(TipoEntrada.ADULTO)==46
    assert group.subtotal_for_type(TipoEntrada.BEBE)==0
