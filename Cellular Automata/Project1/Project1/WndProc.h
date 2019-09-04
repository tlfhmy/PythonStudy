#pragma once

LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
	static int icx, icy;
	static int cxChar, cyChar;
	HDC hdc;
	TEXTMETRIC tm;
	static HWND button[3];

	TCHAR lptemp[1024];

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

		//wsprintf(lptemp, "Length of window:%d,\nHight of window:%d", icx, icy);
		//MessageBox(NULL, lptemp, "Action", MB_OK);
		break;

	case WM_PAINT:
		hdc = GetWindowDC(hwnd);

		MoveToEx(hdc, icx / 2, icy / 2, NULL);
		LineTo(hdc, icx, icy);

		ReleaseDC(hwnd, hdc);

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