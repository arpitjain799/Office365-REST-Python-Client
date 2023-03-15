from office365.entity import Entity


class OrganizationalBrandingProperties(Entity):
    """
    An abstract type that exposes properties for configuring an organization's branding.

    Organizations can customize their Azure Active Directory (Azure AD) sign-in pages which appear when users sign in to
    their organization's tenant-specific apps, or when Azure AD identifies the user's tenant from their username.
    A developer can also read the company's branding information and customize their app experience to tailor
    it specifically for the signed-in user using their company's branding.

    You can't change your original configuration's language as represented by the organizationalBranding object.
    However, companies can add different branding based on locale. For language-specific branding,
    see the organizationalBrandingLocalization object.
    """
