from src.main import *
import pytest
from fastapi import HTTPException

@pytest.mark.asyncio
async def test_criar_tarefa():
    tarefas.clear()
    tarefa_teste = Tarefa(nome="Estudar",id=1,concluida=True)
    result = await criar_tarefa(tarefa_teste)
    assert result == tarefa_teste

@pytest.mark.asyncio
async def test_listar_tarefas():
    tarefas.clear()

    t1 = Tarefa(nome="Estudar",id=1,concluida=True)
    t2 = Tarefa(nome="Praticar",id=2,concluida=False)

    tarefas.extend([t1,t2])

    result = await listar_tarefas()
    assert len(result) == 2
    assert result[0].nome == "Estudar"
    assert result[0].id == 1
    assert result[0].concluida is True
    assert result[1].nome == "Praticar"
    assert result[1].id == 2
    assert result[1].concluida is False



@pytest.mark.asyncio
async def test_obter_tarefa():
    tarefas.clear()
    t1 = Tarefa(nome="Estudar", id=1, concluida=True)
    t2 = Tarefa(nome="Praticar", id=2, concluida=False)

    tarefas.extend([t1, t2])
    result = await obter_tarefa(1)
    assert result is not None
    assert result.id == 1
    assert result.concluida is True
    assert result.nome == "Estudar"

    with pytest.raises(HTTPException) as excinfo:
        await obter_tarefa(3)
        assert excinfo.value.status_code == 404
        assert excinfo.value.detail == "Tarefa não encontrada"


@pytest.mark.asyncio
async def test_atualizar_tarefa_negativo():
    tarefas.clear()
    t1 = Tarefa(nome="Estudar", id=1, concluida=True)
    tarefas.append(t1)

    tarefa_atualizada = Tarefa(nome="Praticar", id=2, concluida=False)
    with pytest.raises(HTTPException):
        await atualizar_tarefa(2, tarefa_atualizada)

@pytest.mark.asyncio
async def test_atualizar_tarefa_positivo():
    tarefas.clear()
    t1 = Tarefa(nome="Estudar", id=1, concluida=True)
    tarefas.append(t1)

    tarefa_atualizada = Tarefa(nome="Praticar", id=1, concluida=False)
    result = await atualizar_tarefa(1, tarefa_atualizada)
    assert result.nome == "Praticar"
    assert result.concluida is False



@pytest.mark.asyncio
async def test_deletar_tarefa_negativo():
    tarefas.clear()
    t1 = Tarefa(nome="Estudar", id=1, concluida=True)
    tarefas.append(t1)

    with pytest.raises(HTTPException):
        await deletar_tarefa(2)



@pytest.mark.asyncio
async def test_deletar_tarefa_positivo():
    tarefas.clear()
    t1 = Tarefa(nome="Estudar", id=1, concluida=True)
    tarefas.extend([t1])
    result = await deletar_tarefa(1)
    assert result

@pytest.mark.asyncio
async def test_listar_tarefas_concluidas():
    tarefas.clear()
    t1 = Tarefa(nome="Estudar", id=1, concluida=True)

    tarefas.extend([t1])
    result = await listar_tarefas_concluidas()
    assert isinstance(result,list)
    assert len(result) == 1
    assert result[0].id== 1
    assert result[0].concluida is True
    assert result[0].nome == "Estudar"
