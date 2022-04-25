from db.db import engine
from models.gem_models import Gem, GemProperties
from sqlmodel import Session, select, or_


def select_all_gems():
    with Session(engine) as session:
        statement = select(Gem, GemProperties).join(GemProperties)
       # statement = statement.where(Gem.id > 0).where(Gem.id < 2)
        #statement = statement.where(or_(Gem.id>1, Gem.price!=2000))
        result = session.exec(statement)
        res = []
        for gem, props in result:
            res.append({'gem': gem, 'props': props})
        return res


def select_gem(id):
    with Session(engine) as session:
        statement = select(Gem, GemProperties).join(GemProperties)
        statement = statement.where(Gem.id==id)
        result = session.exec(statement)
        return result.first()


#select_gems()