# 美術來源與生成記錄

風格：參照使用者提供的 `kosinga_cover_icon.png`，採雕飾金邊、深藍海面、木製船艦、暖金光線與寫實桌遊插畫。

使用 **內建 imagegen 工具**生成兩張原稿，未使用外部 API 或 CLI fallback。
圖集第一次請求遇到認證錯誤，重試後成功；下列為最終採用的提示詞。

## 棋盤原稿：`art/ocean-master.png`

> Use case: stylized-concept. Create a premium illustrated game board BACKGROUND for Koxinga, 1600x900 landscape. Style inspired by lavish historical maritime board game box art: lustrous aged gold, deep peacock blue ocean, warm cream sails, rich carved wood, painterly realistic 3D detail. Top down oblique antique Taiwan coastal chart, a lush emerald island at CENTER, intricate waves and reefs, distant Chinese junk ships and red-roof stone coastal fortress at far edges. Center island occupies x 500-1100 y 200-700. The outer 15 percent around all four edges is mostly clean deep blue sea to overlay route cells. No grid, no route, no tokens, no dice, absolutely NO TEXT or labels. Subtle gold ornamental thin frame right at boundary. Warm cinematic sunlight. Detailed but calm, designed to sit behind readable game UI. Entire canvas filled; no margins.

## 素材圖集：`art/icons-master.png`

> Create a single game sprite atlas: exact 4 columns and 3 rows, equally sized square cells. Landscape 4:3 ratio. Uniform solid midnight blue background, no lines between cells. Each object isolated centered in cell with generous empty margin. Premium realistic painterly Chinese maritime board game miniatures, sculpted gold, navy enamel, warm sunlit wood matching Koxinga naval adventure. NO text, NO numbers. First row: wheat sack, stack of gold coins, iron cannon on carriage, open treasure chest. Second row: Chinese sailing junk, golden compass rose, blue twelve-sided die without markings, flame. Third row: parchment scroll, gold anchor, Ming admiral portrait in gold helmet with red cape, gold laurel crown. Exactly twelve separate objects in this exact grid order, no objects touching neighboring cells. Production ready illustrated UI asset sheet.

## 封面

`art/cover-reference.png` 是使用者提供圖片的原始副本，供開場與應用程式圖示使用。

## 匯出

`tools/build_art.py` 按 `art/legacy-assets.json` 切分圖集、縮放、排版日夜標記、骰子數字及金框，匯出到 `Image/`。
輸出 78 張相容原圖及 12 張較高解析度介面圖，所有執行素材均保存在專案中。
棋盤航線、文字、互動回饋及粒子由 Pygame 在執行時繪製。
