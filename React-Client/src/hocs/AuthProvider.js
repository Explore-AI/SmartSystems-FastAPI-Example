import React from "react";
import { MsalProvider, MsalAuthenticationTemplate } from "@azure/msal-react";
import { InteractionType } from "@azure/msal-browser";
import { msalInstance, msalUserImpersonation } from "../lib/AuthConfig";
import LoadingIcon from "../components/fields/LoadingIcon";

const AuthProvider = (PageComponent) => {
  function HOC() {
    const authRequest = {
      scopes: [msalUserImpersonation],
    };

    return (
      <MsalProvider instance={msalInstance}>
        <MsalAuthenticationTemplate
          interactionType={InteractionType.Redirect}
          authenticationRequest={authRequest}
          loadingComponent={LoadingIcon}
        >
          <PageComponent />
        </MsalAuthenticationTemplate>
      </MsalProvider>
    );
  }
  return HOC;
};

export default AuthProvider;
