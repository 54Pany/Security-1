// ���� ifdef ���Ǵ���ʹ�� DLL �������򵥵�
// ��ı�׼�������� DLL �е������ļ��������������϶���� TDBG_EXPORTS
// ���ű���ġ���ʹ�ô� DLL ��
// �κ�������Ŀ�ϲ�Ӧ����˷��š�������Դ�ļ��а������ļ����κ�������Ŀ���Ὣ
// TDBG_API ������Ϊ�Ǵ� DLL ����ģ����� DLL ���ô˺궨���
// ������Ϊ�Ǳ������ġ�
#ifdef TDBG_EXPORTS
#define TDBG_API __declspec(dllexport)
#else
#define TDBG_API __declspec(dllimport)
#endif

// �����Ǵ� tdbg.dll ������
class TDBG_API Ctdbg {
public:
	Ctdbg(void);
	// TODO: �ڴ�������ķ�����
};

extern TDBG_API int ntdbg;

TDBG_API int fntdbg(void);

#define INIT_API()                             \
	HRESULT Status;                            \
	if ((Status = ExtQuery(Client)) != S_OK) return Status; 


#define EXT_RELEASE(Unk) \
	((Unk) != NULL ? ((Unk)->Release(), (Unk) = NULL) : NULL)

#define EXIT_API ExtRelease

void ExtRelease(void);