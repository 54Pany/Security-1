

shdocvw_calls = [

    "CShdocvwBroker::QueryInterface(_GUID const &,void * *)",
    "CInternetShortcutPropertyStore::AddRef(void)",
    "CShdocvwBroker::Release(void)",
    "CShdocvwBroker::RedirectUrl(ushort const *,ulong,_BROKER_REDIRECT_DETAIL *,IXMicTestMode *)",
    "CShdocvwBroker::RedirectShortcut(ushort const *,ushort const *,ulong,_BROKER_REDIRECT_DETAIL *)",
    "CShdocvwBroker::RedirectUrlWithBindInfo(_BROKER_BIND_INFO *,_BROKER_REDIRECT_DETAIL *,IXMicTestMode *)",
    "CShdocvwBroker::ShowInternetOptions(HWND__ *,ushort const *,ushort const *,long,_ITEMIDLIST_ABSOLUTE * *,ulong,int *)",
    "CShdocvwBroker::ShowInternetOptionsZones(HWND__ *,ushort const *,ushort const *)",
    "CShdocvwBroker::ShowInternetOptionsLanguages(HWND__ *)",
    "CShdocvwBroker::ShowPopupManager(HWND__ *,ushort const *)",
    "CShdocvwBroker::ConfigurePopupExemption(HWND__ *,int,ushort const *,int *)",
    "CShdocvwBroker::ConfigurePopupMgr(HWND__ *,int)",
    "CShdocvwBroker::RemoveFirstHomePage(void)",
    "CShdocvwBroker::SetHomePage(HWND__ *,long,_ITEMIDLIST_ABSOLUTE * *,long)",
    "CShdocvwBroker::RemoveHomePage(HWND__ *,int)",
    "CShdocvwBroker::FixInternetSecurity(HWND__ *,int *)",
    "CShdocvwBroker::ShowManageAddons(HWND__ *,ulong,_GUID *,uint,int)",
    "CShdocvwBroker::CacheExtFileVersion(_GUID const &,ushort const *)",
    "CShdocvwBroker::ShowAxApprovalDlg(HWND__ *,_GUID const &,int,ushort const *,ushort const *,ushort const *)",
    "CShdocvwBroker::SendLink(_ITEMIDLIST_ABSOLUTE const *,ushort const *)",
    "CShdocvwBroker::SendPage(HWND__ *,IDataObject *)",
    "CShdocvwBroker::NewMessage(void)",
    "CShdocvwBroker::ReadMail(HWND__ *)",
    "CShdocvwBroker::SetAsBackground(ushort const *)",
    "CShdocvwBroker::ShowSaveBrowseFile(HWND__ *,ushort const *,ushort const *,int,int,ushort * *,ulong *,ulong *)",
    "CShdocvwBroker::SaveAsComplete(void)",
    "CShdocvwBroker::SaveAsFile(void)",
    "CShdocvwBroker::StartImportExportWizard(int,HWND__ *)",
    "CShdocvwBroker::EditWith(HWND__ *,ulong,ulong,ulong,ushort const *,ushort const *,ushort const *)",
    "CShdocvwBroker::ShowSaveImage(HWND__ *,ushort const *,ulong,ushort * *)",
    "CShdocvwBroker::SaveImage(ushort const *)",
    "CShdocvwBroker::CreateShortcutOnDesktop(HWND__ *,_ITEMIDLIST_ABSOLUTE const *,ushort const *,IOleCommandTarget *)",
    "CShdocvwBroker::ShowSynchronizeUI(void)",
    "CShdocvwBroker::OpenFolderAndSelectItem(ushort const *)",
    "CShdocvwBroker::DoGetOpenFileNameDialog(_SOpenDlg *)",
    "CShdocvwBroker::ShowSaveFileName(HWND__ *,ushort const *,ushort const *,ushort const *,ushort const *,uint,ushort *,ulong,ushort const *,ushort * *)",
    "CShdocvwBroker::SaveFile(HWND__ *,uint,ulong)",
    "CShdocvwBroker::VerifyTrustAndExecute(HWND__ *,ushort const *,ushort const *)",
    "CShdocvwBroker::GetFeedByUrl(ushort const *,ushort * *)",
    "CShdocvwBroker::BrokerAddToFavoritesEx(HWND__ *,_ITEMIDLIST_ABSOLUTE const *,ushort const *,ulong,IOleCommandTarget *,ushort *,ulong,ushort const *)",
    "CShdocvwBroker::Subscribe(HWND__ *,ushort const *,ushort const *,int,int,int)",
    "CShdocvwBroker::MarkAllItemsRead(ushort const *)",
    "CShdocvwBroker::MarkItemsRead(ushort const *,uint *,uint)",
    "CShdocvwBroker::Properties(HWND__ *,ushort const *)",
    "CShdocvwBroker::DeleteFeedItem(HWND__ *,ushort const *,uint)",
    "CShdocvwBroker::DeleteFeed(HWND__ *,ushort const *)",
    "CShdocvwBroker::DeleteFolder(HWND__ *,ushort const *)",
    "CShdocvwBroker::Refresh(ushort const *)",
    "CShdocvwBroker::MoveFeed(HWND__ *,ushort const *,ushort const *)",
    "CShdocvwBroker::MoveFeedFolder(HWND__ *,ushort const *,ushort const *)",
    "CShdocvwBroker::RenameFeed(HWND__ *,ushort const *,ushort const *)",
    "CShdocvwBroker::RenameFeedFolder(HWND__ *,ushort const *,ushort const *)",
    "CShdocvwBroker::NewFeedFolder(ushort const *)",
    "CShdocvwBroker::FeedRefreshAll(void)",
    "CShdocvwBroker::ShowFeedAuthDialog(HWND__ *,ushort const *,tagFEEDTASKS_AUTHTYPE)",
    "CShdocvwBroker::ShowAddSearchProvider(HWND__ *,ushort const *,ushort const *,int)",
    "CShdocvwBroker::InitHKCUSearchScopesRegKey(void)",
    "CShdocvwBroker::DoShowDeleteBrowsingHistoryDialog(HWND__ *)",
    "CShdocvwBroker::ResetInternetOptions(void)",
    "CShdocvwBroker::StartAutoProxyDetection(void)",
    "CShdocvwBroker::ForceNexusLookup(void)",
    "CShdocvwBroker::SetAutoConnectOption(ushort const *,ulong)",
    "CShdocvwBroker::EditAntiPhishingOptinSetting(HWND__ *,ulong,int *)",
    "CShdocvwBroker::ShowMyPictures(void)",
    "CShdocvwBroker::ChangeIntranetSettings(HWND__ *,int)",
    "CShdocvwBroker::FixProtectedModeSettings(void)",
    "CShdocvwBroker::ShowAddService(HWND__ *,ushort const *,ushort const *,int)",
    "CShdocvwBroker::ShowAddWebFilter(HWND__ *,ushort const *,ushort const *,ushort const *)",
    "CShdocvwBroker::DoBrowserRegister(IDispatch *,long,int,long *)",
    "CShdocvwBroker::DoBrowserRevoke(long)",
    "CShdocvwBroker::DoOnNavigate(long,tagVARIANT *)",
    "CWebPreviewDispatch::AddDesktopComponent(ushort *,ushort *,tagVARIANT *,tagVARIANT *,tagVARIANT *,tagVARIANT *)",
    "CShdocvwBroker::DoOnCreated(long,IUnknown *)",
    "CShdocvwBroker::GetShellWindows(IUnknown * *)",
    "CClosedTabManager::RestoreTab(long,ulong,long)",
    "CPublicTravelLogCreateHelper::SetPositionCookie(ulong)",
    "CShdocvwBroker::IsProtectedModeUrl(ushort const *)",
    "CShdocvwBroker::DoDiagnoseConnectionProblems(HWND__ *,ushort *,ushort *)",
    "CShdocvwBroker::PerformDoDragDrop(HWND__ *,IEDataObjectWrapper *,IEDropSourceWrapper *,ulong,ulong,ulong *,long *)",
    "CShdocvwBroker::TurnOnFeedSyncEngine(HWND__ *)",
    "CShdocvwBroker::InternetSetPerSiteCookieDecisionW(ushort const *,ulong)",
    "CShdocvwBroker::ConfirmCookie(HWND__ *,ulong,ulong,_BROKER_COOKIE_DLG_INFO *)",
    "CShdocvwBroker::SetAttachmentUserOverride(ushort const *)",
    "CShdocvwBroker::WriteClassesOfCategory(_GUID const &,int)",
    "CShdocvwBroker::BrokerSetFocus(ulong,HWND__ *)",
    "CShdocvwBroker::BrokerShellNotifyIconA(ulong,_BROKER_NOTIFYICONDATAA *)",
    "CShdocvwBroker::BrokerShellNotifyIconW(ulong,_BROKER_NOTIFYICONDATAW *)",
    "CShdocvwBroker::DisplayVirtualizedFolder(void)",
    "CShdocvwBroker::BrokerSetWindowPos(HWND__ *,HWND__ *,int,int,int,int,uint)",
    "CShdocvwBroker::WriteUntrustedControlDetails(_GUID const &,ushort const *,ushort const *,ulong,uchar *)",
    "CShdocvwBroker::SetComponentDeclined(char const *,char const *)",
    "CShdocvwBroker::DoShowPrintDialog(_BROKER_PRINTDLG *)",
    "CShdocvwBroker::NavigateHomePages(void)",
    "CShdocvwBroker::ShowAxDomainApprovalDlg(HWND__ *,_GUID const &,int,ushort const *,ushort const *,ushort const *,ushort const *)",
    "CShdocvwBroker::ActivateExtensionFromCLSID(HWND__ *,ushort const *,ulong,uint,uint)",
    "CShdocvwBroker::BrokerCoCreateNewIEWindow(ulong,_GUID const &,void * *,int,ulong)",
    "CShdocvwBroker::BeginFakeModalityForwardingToTab(HWND__ *,long)",
    "CShdocvwBroker::BrokerEnableWindow(int,int *)",
    "CShdocvwBroker::EndFakeModalityForwardingToTab(HWND__ *,long)",
    "CShdocvwBroker::CloseOldTabIfFailed(void)",
    "CShdocvwBroker::GetGuidsForConnectedNetworks(ulong *,ushort * * *,ushort * * *,ushort * * *,ulong *,ulong *)",
    "CShdocvwBroker::EnableSuggestedSites(HWND__ *,int)",
    "CShdocvwBroker::SetProgressValue(HWND__ *,ulong,ulong)",
    "CShdocvwBroker::BrokerStartNewIESession(void)",
    "CShdocvwBroker::CompatDetachInputQueue(HWND__ *)",
    "CShdocvwBroker::CompatAttachInputQueue(void)",
    "CShdocvwBroker::SetToggleKeys(ulong)",
    "CShdocvwBroker::RepositionInfrontIE(HWND__ *,int,int,int,int,uint)",
    "CShdocvwBroker::AddSessionIE7Rule(ushort const *)",
    "CShdocvwBroker::ReportShipAssert(ulong,ulong,ulong,ushort const *,ushort const *,ushort const *)",
    "CShdocvwBroker::AutoProxyGetProxyForUrl(tagProxyResolveUrl *,tagProxyResult *)",
    "CShdocvwBroker::AutoProxyReportRequestResults(int,tagProxyResolveUrl *,tagProxyResult *)",
    "CShdocvwBroker::ShowOpenSafeOpenDialog(HWND__ *,_BROKER_SAFEOPENDLGPARAM *,uint *,uint *)",
    "CShdocvwBroker::BrokerAddSiteToStartMenu(HWND__ *,ushort *,ushort const *,long,ulong)",
    "CShdocvwBroker::SiteModeAddThumbnailButton(uint *,HWND__ *,ushort *,ushort const *)",
    "CShdocvwBroker::SiteModeAddButtonStyle(int *,HWND__ *,uint,ushort *,ushort const *)",
    "CShdocvwBroker::IsSiteModeFirstRun(int,ushort *)",
    "CShdocvwBroker::BrokerDoSiteModeDragDrop(ulong,long *,ulong *)",
    "CShdocvwBroker::EnterUILock(long)",
    "CShdocvwBroker::LeaveUILock(long)",
    "CShdocvwBroker::`vector deleting destructor'(uint)" 
]


ierecovery_store_calls = [

    "TUnknownMT3<IRecoveryStore,ICookieJarRecoveryData,ICredentialRecoveryData>::QueryInterface(_GUID const &,void * *)",
    "TUnknownMT2<ITabRecoveryData,ITravelLogRecoveryData>::AddRef(void)",
    "TUnknownMT2<IBindStatusCallback,IHttpNegotiate>::Release(void)",
    "CRecoveryStore::Initialize(ulong,__MIDL___MIDL_itf_recoverystore_0000_0006_0001,ulong,ushort const *)",
    "CRecoveryStore::InitializeFromFile(ushort const *,__MIDL___MIDL_itf_recoverystore_0000_0006_0001,ulong)",
    "CRecoveryStore::CreateFrame(uint *,ulong,ulong)",
    "CRecoveryStore::CloseFrame(uint)",
    "CRecoveryStore::GetFrameCount(uint *)",
    "CRecoveryStore::GetFrameId(uint,uint *)",
    "CRecoveryStore::GetFrameIESession(uint,ulong *,ulong *)",
    "CRecoveryStore::CreateTab(uint,ushort const *,ITabRecoveryData * *)",
    "CRecoveryStore::CloseTab(uint,_GUID const &)",
    "CRecoveryStore::GetTabCount(uint,uint *)",
    "CRecoveryStore::GetTab(uint,uint,ITabRecoveryData * *)",
    "CLinksMonitor::GetCount(long *)",
    "CRecoveryStore::GetClosedTab(_GUID const &,ITabRecoveryData * *)",
    "CRecoveryStore::DeleteClosedTab(_GUID const &)",
    "CRecoveryStore::Recover(ITabWindowManager *,ulong)",
    "CRecoveryStore::RecoverFrame(ITabWindowManager *,ulong,uint)",
    "CRecoveryStore::Flush(void)",
    "CRecoveryStore::DeleteSelf(void)",
    "CRecoveryStore::DeleteAllTabs(void)",
    "CRecoveryStore::DeleteOnLastRelease(void)",
    "CRecoveryStore::Shutdown(void)",
    "CRecoveryStore::Restart(void)",
    "CRecoveryStore::IsShutdown(int *)",
    "CRecoveryStore::IsRestart(int *)",
    "CTabWindow::GetID(long *)",
    "CRecoveryStore::IsInPrivate(int *)",
    "CRecoveryStore::IsExtOff(int *)",
    "CRecoveryStore::GetFrameCLSID(_GUID *)",
    "CRecoveryStore::SetActiveTab(uint,_GUID const &)",
    "CRecoveryStore::GetActiveTab(uint,_GUID *)",
    "CRecoveryStore::SwitchTabFrame(uint,uint,_GUID const &)",
    "CRecoveryStore::DeleteExistingStores(void)",
    "CRecoveryStore::FindCrashedSessions(int *,int *)"]



settingsstore_calls = [
    "TUnknownMT1<ISettingsBroker>::QueryInterface(_GUID const &,void * *)",
    "TUnknownMT1<ISettingsBroker>::AddRef(void)",
    "TUnknownMT1<ISettingsBroker>::Release(void)",
    "SettingStore::CSettingsBroker::SetValue(_GUID const &,int,int,uchar *,ulong)",
    "SettingStore::CSettingsBroker::SetExtValue(_GUID const &,int,int,tagSAFEARRAY *,uchar *,ulong)",
    "SettingStore::CSettingsBroker::DeleteValue(_GUID const &,int)",
    "SettingStore::CSettingsBroker::DeleteExtValue(_GUID const &,int,tagSAFEARRAY *)",
    "SettingStore::CSettingsBroker::DeleteKey(_GUID const &,int)",
    "SettingStore::CSettingsBroker::DeleteExtKey(_GUID const &,int,tagSAFEARRAY *)" ]

ieuser_calls = [
    "CIEUserBrokerObject::QueryInterface(_GUID const &,void * *)",
    "CIEUserBrokerObject::AddRef(void)",
    "CIEUserBrokerObject::Release(void)",
    "CIEUserBrokerObject::Initialize(HWND__ *,ushort const *,ulong *)",
    "CIEUserBrokerObject::CreateProcessW(ulong,ushort *,ushort *,ulong,ulong,uchar const *,ushort *,_BROKER_STARTUINFOEXW *,_PROCESS_INFORMATION *)",
    "CIEUserBrokerObject::WinExec(ulong,char const *,uint,uint *)",
    "CIEUserBrokerObject::BrokerCreateKnownObject(_GUID const &,_GUID const &,IUnknown * *)",
    "CIEUserBrokerObject::BrokerCoCreateInstance(ulong,_GUID const &,IUnknown *,ulong,_GUID const &,IUnknown * *)",
    "CIEUserBrokerObject::BrokerCoCreateInstanceEx(ulong,_GUID const &,IUnknown *,ulong,_COSERVERINFO *,ulong,tagBROKER_MULTI_QI *)",
    "CIEUserBrokerObject::BrokerCoGetClassObject(ulong,_GUID const &,ulong,_COSERVERINFO *,_GUID const &,IUnknown * *)"]


stdidentity_unk_calls = [
    "CStdIdentity::CInternalUnk::QueryInterface(_GUID const &,void * *)",
    "CStdIdentity::CInternalUnk::AddRef(void)",
    "CStdIdentity::CInternalUnk::Release(void)",
    "CStdIdentity::CInternalUnk::QueryInternalInterface(_GUID const &,void * *)"]


ieaxinstall_calls = [
    "CIEUserBrokerObject::QueryInterface`adjustor{12}' (_GUID const &,void * *)",
    "CIEUserBrokerObject::AddRef`adjustor{12}' (void)",
    "CIEUserBrokerObject::Release`adjustor{12}' (void)",
    "CIEUserBrokerObject::BrokerGetAxInstallBroker(_GUID const &,_GUID const &,HWND__ *,ulong,IUnknown * *)"]

iereghelperbroker_calls = [
    "CIEUserBrokerObject::QueryInterface`adjustor{4}' (_GUID const &,void * *)",
    "CIEUserBrokerObject::AddRef`adjustor{4}' (void)",
    "CIEUserBrokerObject::Release`adjustor{4}' (void)",
    "CIEUserBrokerObject::DoDelSingleValue(ulong)",
    "CIEUserBrokerObject::DoDelIndexedValue(ulong,ulong)",
    "CIEUserBrokerObject::DoSetSingleValue(ulong,uchar *,ulong)",
    "CIEUserBrokerObject::DoSetIndexedValue(ulong,ulong,uchar *,ulong)",
    "CFeedViewer::CFeedMoniker::Reduce(IBindCtx *,ulong,IMoniker * *,IMoniker * *)",
    "CIEUserBrokerObject::DoCreateKey(ulong)"]

iereghelperobject_cleanup_calls = [
    "[thunk]:CIEUserBrokerObject::QueryInterface`adjustor{8}' (_GUID const &,void * *)",
    "[thunk]:CIEUserBrokerObject::AddRef`adjustor{8}' (void)",
    "[thunk]:CIEUserBrokerObject::Release`adjustor{8}' (void)",
    "CIEUserBrokerObject::RegisterCleanup(IEBrokerObjectCleanup *)"]


iebrokerattach_calls = [
    "[thunk]:CIEUserBrokerObject::QueryInterface`adjustor{16}' (_GUID const &,void * *)",
    "[thunk]:CIEUserBrokerObject::AddRef`adjustor{16}' (void)",
    "[thunk]:CIEUserBrokerObject::Release`adjustor{16}' (void)",
    "CIEUserBrokerObject::AttachIEFrameToBroker(IUnknown *)" ]

protectedmodeAPI_calls = [
    "CProtectedModeAPI::QueryInterface(_GUID const &,void * *)",
    "CHeadBSC::AddRef(void)",
    "CProtectedModeAPI::Release(void)",
    "CProtectedModeAPI::ShowSaveFileDialog(HWND__ *,ushort const *,ushort const *,ushort const *,ushort const *,ulong,ulong,ushort * *)",
    "CProtectedModeAPI::SaveFileAs(ushort const *)",
    "CProtectedModeAPI::RegCreateKeyExW(ulong,ushort const *,ulong,ulong *,ulong *)",
    "CProtectedModeAPI::RegSetValueExW(ushort const *,ushort const *,ulong,uchar const *,ulong)",
    "CProtectedModeAPI::`vector deleting destructor'(uint)" ]


feedsloribroker_calls = [
    "FeedsLoriBroker::QueryInterface()",
    "FeedsLoriBroker::AddRef()",
    "FeedsLoriBroker::Release()",
    "FeedsLoriBroker::Func3()",
    "FeedsLoriBroker::Func4()",
    "FeedsLoriBroker::Func5()",
    "FeedsLoriBroker::Func6()",
    "FeedsLoriBroker::Func7()",
    "FeedsLoriBroker::Func8()",
    "FeedsLoriBroker::Func9()",
    "FeedsLoriBroker::Func10()"]

feedsarbiterloribroker_calls = [
    "FeedsArbiterLoriBroker::QueryInterface()",
    "FeedsArbiterLoriBroker::AddRef()",
    "FeedsArbiterLoriBroker::Release()",
    "FeedsArbiterLoriBroker::Func3()",
    "FeedsArbiterLoriBroker::Func4()"]

shellwindow_calls = [
    "CLCIE_IIDProxy_IShellWindows::QueryInterface`adjustor{40}' (_GUID const &,void * *)",
    "CLCIE_IIDProxy_IWebBrowser2::AddRef`adjustor{40}' (void)",
    "CLCIE_IIDProxy_IHTMLPrivateWindow3::Release`adjustor{40}' (void)",
    "CLCIE_IIDProxy_IHTMLDocument2::get_alinkColor(tagVARIANT *)",
    "CLCIE_IIDProxy_IShellBrowser::SetMenuSB(HMENU__ *,void *,HWND__ *)",
    "CLCIE_IIDProxy_IIETravelLog2::UpdateEntryEx(IUnknown *,int,int,int,int)",
    "CLCIE_IIDProxy_IDispatch::Invoke(long,_GUID const &,ulong,ushort,tagDISPPARAMS *,tagVARIANT *,tagEXCEPINFO *,uint *)",
    "CLCIE_IIDProxy_IHTMLDocument2::get_alinkColor(tagVARIANT *)",
    "CLCIE_IIDProxy_IIETravelLog2::UpdateEntryEx(IUnknown *,int,int,int,int)",
    "CLCIE_IIDProxy_IWebBrowserPriv2::SetSearchTerm(ushort *)",
    "CLCIE_IIDProxy_IShellWindows::Register(IDispatch *,long,int,long *)",
    "CLCIE_IIDProxy_IShellWindows::RegisterPending(long,tagVARIANT *,tagVARIANT *,int,long *)",
    "CLCIE_IIDProxy_IShellWindows::Revoke(long)",
    "CLCIE_IIDProxy_ITravelLog::AddEntry(IUnknown *,int)",
    "CLCIE_IIDProxy_ITravelLog::AddEntry(IUnknown *,int)",
    "CLCIE_IIDProxy_IShellWindows::FindWindowSW(tagVARIANT *,tagVARIANT *,int,long *,int,IDispatch * *)",
    "CLCIE_IIDProxy_IShellWindows::OnCreated(long,IUnknown *)",
    "CLCIE_IIDProxy_IHTMLDocument2::get_alinkColor(tagVARIANT *)"]




def get_shdocvw_calls_name():
    return shdocvw_calls

def get_ierecovery_store_calls_name():
    return ierecovery_store_calls

def get_settingsstore_calls_name():
    return settingsstore_calls

def get_ieuser_calls_name():
    return ieuser_calls

def get_stdidentity_unk_calls_name():
    return stdidentity_unk_calls

def get_ieaxinstall_calls_name():
    return ieaxinstall_calls

def get_iereghelperbroker_calls_name():
    return iereghelperbroker_calls

def get_iereghelperobject_cleanup_calls_name():
    return iereghelperobject_cleanup_calls

def get_iebrokerattach_calls_name():
    return iebrokerattach_calls

def get_protectedmodeAPI_calls_name():
    return protectedmodeAPI_calls


def get_feedsloribroker_calls_name():
    return feedsloribroker_calls

def get_feedsarbiterloribroker_calls_name():
    return feedsarbiterloribroker_calls


def get_shellwindow_calls_name():
    return shellwindow_calls
