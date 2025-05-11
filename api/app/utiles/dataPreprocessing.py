def processForDB(baseObject, fullModel) -> dict:
    """
    :param baseObject: BaseModel classobject
    :param fullModel: BaseModel class
    :return: dict without objId field
    """
    return fullModel(**baseObject.model_dump()).model_dump(exclude={"objId"})