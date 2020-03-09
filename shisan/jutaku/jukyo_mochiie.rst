========================================
持ち家（一戸建て・マンション）について
========================================

昨年10月1日以降に転居して現在持ち家に住んでいる方、もしくは現在住んでいる土地・住宅を購入・増改築・名義変更した方に聞いています。

.. raw:: html

 <table border="1 #093350">
 <thead>
 <tr>
 <th>敷地取得年</th>
 <th>住宅取得年</th>
 <th>住宅建築時期</th>
 </tr>
 <tbody>
 <tr>
 <td><a href="../../variable/Q889.html">Q889</a></td>
 <td><a href="../../variable/Q890.html">Q890</a></td>
 <td><a href="../../variable/Q891.html">Q891</a></td>
 </tr>
 </tbody>
 </table>

.. note:: 第6回までは、「住宅取得年」は :doc:`Q376A </variable/Q376A>`、「住宅建築時期」は :doc:`Q376B </variable/Q376B>` にて聞いていました。

   調査票では元号でたずねていますが、レコードでは西暦下2桁に変換しています。


.. raw:: html

 <table border="1 #093350">
 <thead>
 <tr>
 <th colspan="3">敷地</th>
 <th colspan="3">住宅</th>
 </tr>
 </thead>

 <tbody>
 <tr>
 <td colspan="2" rowspan="2" style="vertical-align:middle;">敷地面積</td>
 <td rowspan="2" style="vertical-align:middle;"><a href="../../variable/Q375B.html">Q375B</a></td>
 <td rowspan="2" style="vertical-align:middle;">延べ床面積</td>
 <td>（実数）</td>
 <td><a href="../../variable/Q802.html">Q802</a></td>
 </tr>
 <tr>
 <td>（カテゴリー）</td>
 <td><a href="../../variable/Q372.html">Q372</a></td>
 </tr>
 <tr>
 <td rowspan="2" style="vertical-align:middle;">敷地の名義人</td>
 <td>有配偶</td>
 <td><a href="../../variable/Q375C.html">Q375C</a></td>
 <td rowspan="2" style="vertical-align:middle;">住宅の名義人</td>
 <td>有配偶</td>
 <td><a href="../../variable/Q376C.html">Q376C</a></td>
 </tr>
 <td>無配偶</td>
 <td><a href="../../variable/Q375D.html">Q375D</a></td>
 <td>無配偶</td>
 <td><a href="../../variable/Q376D.html">Q376D</a></td>
 </tr>
 <tr>
 <td colspan="2">敷地取得の方法</br>（本人・配偶者名義の場合）</td>
 <td style="vertical-align:middle;"><a href="../../variable/Q375E.html">Q375E</a></td>
 <td colspan="2">住宅取得の方法</br>（本人・配偶者名義の場合）</td>
 <td style="vertical-align:middle;"><a href="../../variable/Q376E.html">Q376E</a></td>
 </tr>
 <tr>
 <td colspan="2">敷地取得に関与した親</br>（親の関与があった場合）</td>
 <td style="vertical-align:middle;"><a href="../../variable/Q375F.html">Q375F</a></td>
 <td colspan="2">住宅取得に関与した親</br>（親の関与があった場合）</td>
 <td style="vertical-align:middle;"><a href="../../variable/Q376F.html">Q376F</a></td>
 </tr>
 </tbody>
 </table>

.. note::   :doc:`Q372 </variable/Q372>` は延べ床面積の実数をカテゴリー別にリコーディングしたものです。


.. warning:: 下記のように、第10回以降の「敷地の名義人（:doc:`Q375C </variable/Q375C>` 、 :doc:`Q375D </variable/Q375D>`）」の選択肢は第1～第9回と異なり、さらに複数回答となっています。ただし回答コードは第1～第9回に合わせてデータ処理しています。


.. raw:: html

  <table border="1 #093350">
  <thead>
  <tr>
  <th colspan="4">第1～第9回</th>
  <th colspan="4">第10回以降</th>
  </tr>
  <tr>
  <th colspan="2">有配偶</th>
  <th colspan="2">無配偶</th>
  <th colspan="2">有配偶</th>
  <th colspan="2">無配偶</th>
  </tr>
  <tr>
  <th width="15%">選択肢</th>
  <th width="10%">コード</th>
  <th width="15%">選択肢</th>
  <th width="10%">コード</th>
  <th width="15%">選択肢</th>
  <th width="10%">コード</th>
  <th width="15%">選択肢</th>
  <th width="10%">コード</th>
  </tr>
  </thead>

  <tbody>
  <tr>
  <td>1.妻</br>2.夫</br>3.妻と夫の共同名義</br>4.妻又は夫といずれかの親との共同名義</br>5.妻の親</br>6.夫の親</br>7.その他</br>8.わからない</td>
  <td>選択肢と同じ</td>
  <td> 1.あなた本人</br>2.親との共同名義</br>3.親の名義</br>4.その他</br>5.わからない</td>
  <td>選択肢と同じ</td>
  <td>1.あなた本人</br>2.ご主人</br>3.あなたの親</br>4.ご主人の親</br>5.その他</br>6.わからない</td>
  <td>1.に〇→1</br>2.に〇→2</br>3.に〇→5</br>4.に〇→6</br>1.と2.に〇→3</br>1.もしくは2.と3.もしくは4に〇→4</br>5.に〇→7</br>6.に〇→8</td>
  <td> 1.あなた本人</br>2.親</br>3.その他</br>4.わからない</td>
  <td>1.に〇→1</br>2.に〇→3</br>1.と2.に〇→3</br>2.に〇→2</br>3.に〇→4</br>4.に〇→5</td>
  </tr>
  </tbody>
  </table>


.. toctree::
   :maxdepth: 1
   :hidden:

   ../variable/Q375B
   ../variable/Q375C
   ../variable/Q375D
   ../variable/Q375E
   ../variable/Q375F
   ../variable/Q802
   ../variable/Q372
   ../variable/Q376C
   ../variable/Q376D
   ../variable/Q376E
   ../variable/Q376F
   ../variable/Q889
   ../variable/Q890
   ../variable/Q891
