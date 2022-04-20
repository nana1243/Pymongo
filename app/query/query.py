from typing import Any, Dict, List

from pydantic import BaseModel

OPERATOR_SEP = "__"


class Query(BaseModel):
    genre__eq: List[str]

    @property
    def pipeline(self) -> List[Dict[str, Any]]:
        result = []
        result.append(self.lookup_pipeline())
        return result

    # left outer join 의 역할을 함.
    def lookup_pipeline(self):
        result = {
            "$lookup": {
                "from": "sp_template",  # join할 collection 명
                "localField": "_id",  #
                "foreignField": "template_id",
                "as": "sp_template",  # 불려질 이름 (`as` 라고 생각하면됨)
            }
        }
        return result
