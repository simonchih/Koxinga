# Koxinga 國姓爺

Pygame 電子桌遊：一名玩家與五支電腦艦隊，在隨機配置的航路上收集資源、爭奪寶藏並進行海戰。

## 啟動

Windows 可直接雙擊 `start_game.bat`。本工作區已建立 `.venv` 並安裝執行依賴。

其他電腦首次使用：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe koxinga.py
```

開場按 Enter 或點「啟航」。**開場按 F1 開啟開始選單**，可選「開始遊戲」、「遊戲教學」、「返回封面」或「離開遊戲」。封面也可直接點「遊戲教學」。
教學提供 15 段詳細說明與操作練習，包括日夜骰、選牌、船艙、停靠費、分岔、寶藏、海戰、掠奪與計分。完成每節操作後解鎖下一步，可返回或重練；教學不影響正式對局。教學中 F1／Esc 返回選單，完成後可直接開始遊戲。
正式遊戲中玩家為艦隊 1；F1 開關簡要操作說明，Esc 離開。
視窗可調整大小，棋盤依比例縮放，滑鼠座標會同步換算。沒有音效裝置仍可執行。

## 美術更新

- `Image/` 原有 78 張圖片全部替換，保留檔名、格式和尺寸以相容原規則程式。
- 新增 12 張 `ui_*.png` 素材，用於資源標記、人物、海戰火焰與介面。
- 航海地圖及圖集由內建 imagegen 生成；使用者提供的圖片用於開場封面與程式圖示。
- 金框、深藍海洋、中文介面、回合光環、船尾水波、海戰及資源粒子統一重製。
- 移除多執行緒繪圖與逐像素阻塞動畫，改在主執行緒繪製，限制 60 FPS。
- 字型快取、資源絕對路徑、等比縮放與打包資源清單已更新。

原遊戲規則和 AI 決策保留。完整規則另見專案原有 PDF 說明書。

美術來源和提示詞：[art/ART_DIRECTION.md](art/ART_DIRECTION.md)。
重建所有遊戲素材：

```powershell
.\.venv\Scripts\python.exe tools/build_art.py
```

## 驗證

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe tests/full_game.py 42
.\.venv\Scripts\python.exe tests/full_game.py 1661
```

14 項整合測試涵蓋 78 張圖片、出牌確認、分岔、抵達終點、火焰骰、資源扣除、計分、說明暫停、開場及縮放座標，以及教學全部步驟、錯誤答案、重練、選單導覽和文字排版。
完整 AI 測試執行實際主迴圈與移動邏輯，但每 90 次才渲染一幀以加快驗證。
另以正常逐幀渲染完成一場 8,903 幀電腦對局，並實際開啟原生視窗驗證啟動。

可重現的展示／截圖：

```powershell
.\.venv\Scripts\python.exe koxinga.py --skip-title --seed 2 --frames 120 --screenshot art/native-preview.png
```

`--autoplay` 將六支艦隊全部交給 AI；`--frames` 限制執行幀數。
環境變數 `KOXINGA_FAST=1` 僅供測試取消幀率限制和回合停頓。
`koxinga.spec` 已包含圖片、封面、音效與字型；本次未建置獨立 EXE。
