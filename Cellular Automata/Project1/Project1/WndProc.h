#pragma once

LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
	static int icx, icy;
	static int cxChar, cyChar;
	HDC hdc;
	TEXTMETRIC tm;
	static HWND button[3];
	//static PTCHAR szBtName[] = { TEXT("Heap Sort"),TEXT("***Sort"),TEXT("***Sort") };



	switch (msg)
	{
	case WM_CREATE:
		hdc = GetDC(hwnd);

		GetTextMetrics(hdc, &tm);
		cxChar = tm.tmAveCharWidth;
		cyChar = tm.tmHeight + tm.tmExternalLeading;

		ReleaseDC(hwnd, hdc);
		break;

	case WM_SIZE:
		icx = LOWORD(lParam);
		icy = HIWORD(lParam);

		//MessageBox(NULL,TEXT())
		break;

	case WM_DESTROY:

		PostQuitMessage(0);
		break;

	default:
		DefWindowProc(hwnd, msg, wParam, lParam);
		break;
	}

	return DefWindowProc(hwnd, msg, wParam, lParam);
}