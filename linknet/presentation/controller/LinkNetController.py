# presentation
import re
from presentation.schema.LinkNet import LinkNet
# application
from application.usecase.LinkNetUseCase import LinkNetUseCase

class LinkNetController:

    def linknet(scm: LinkNet):
        usecase = LinkNetUseCase()
        result = usecase.construct(scm.line_cd, scm.direction_cd, scm.fmp)

        if result:
            print(usecase.linknet)
            print(usecase.linknet.hubs)
            return True