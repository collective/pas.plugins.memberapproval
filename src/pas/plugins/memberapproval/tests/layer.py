from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting
# from plone.testing import z2

from zope.configuration import xmlconfig

class MemberApprovalTestSuite(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import pas.plugins.memberapproval
        xmlconfig.file('configure.zcml', pas.plugins.memberapproval, context=configurationContext)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        # applyProfile(portal, 'pas.plugins.memberapproval:default')
        pass

    def tearDownZope(self, app):
        pass



MEMBERAPPROVAL_FIXTURE = MemberApprovalTestSuite()
MEMBERAPPROVAL_INTEGRATION_TESTING = IntegrationTesting(
                                        bases=(MEMBERAPPROVAL_FIXTURE,),
                                        name="MemberApproval:Integration"
                                    )
MEMBERAPPROVAL_FUNCTIONAL_TESTING = FunctionalTesting(
                                        bases=(MEMBERAPPROVAL_FIXTURE,),
                                        name="MemberApproval:Functional"
                                    )
