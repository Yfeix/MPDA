# MPDA
# Dataset
The dataset we are using is a collection of 29 vulnerabilities from the Juliet Test Suite dataset. The vulnerability names and number of functions are shown in the following figure. You can find them in the https://github.com/find-sec-bugs/juliet-test-suite.

<table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border:none;mso-border-alt:solid windowtext .5pt;
 mso-yfti-tbllook:1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt">
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:14.9pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;mso-border-alt:
  solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.9pt">
  <p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:110%;font-family:&quot;Calibri&quot;,sans-serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;;mso-bidi-font-family:&quot;Times New Roman&quot;;
  mso-ansi-language:IT">CWE</span></b><b style="mso-bidi-font-weight:normal"><span lang="IT" style="font-size:10.5pt;mso-bidi-font-size:10.0pt;line-height:110%;
  font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT;mso-fareast-language:
  ZH-CN"><o:p></o:p></span></b></p>
  </td>
  <td width="291" style="width:218.1pt;border:solid windowtext 1.0pt;border-left:
  none;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.9pt">
  <p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:110%;font-family:&quot;Calibri&quot;,sans-serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;;mso-bidi-font-family:&quot;Times New Roman&quot;;
  mso-ansi-language:IT">Name</span></b><b style="mso-bidi-font-weight:normal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:110%;font-family:&quot;Calibri&quot;,sans-serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;;mso-bidi-font-family:&quot;Times New Roman&quot;;
  mso-bidi-theme-font:minor-bidi;mso-ansi-language:IT"><o:p></o:p></span></b></p>
  </td>
  <td width="158" style="width:118.7pt;border:solid windowtext 1.0pt;border-left:
  none;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.9pt">
  <p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:110%;font-family:&quot;Calibri&quot;,sans-serif;
  mso-fareast-font-family:&quot;Times New Roman&quot;;mso-bidi-font-family:&quot;Times New Roman&quot;;
  mso-ansi-language:IT">Number</span></b><b style="mso-bidi-font-weight:normal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:110%;font-family:&quot;Calibri&quot;,sans-serif;
  mso-fareast-font-family:宋体;mso-fareast-theme-font:minor-fareast;mso-bidi-font-family:
  &quot;Times New Roman&quot;;mso-ansi-language:IT;mso-fareast-language:ZH-CN"> </span></b><b style="mso-bidi-font-weight:normal"><span lang="IT" style="mso-bidi-font-size:
  10.0pt;line-height:110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:
  &quot;Times New Roman&quot;;mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:
  IT">of Functions<o:p></o:p></span></b></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE113<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">HTTP Response
  Splitting<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">8442<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2;height:15.3pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.3pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE129<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:15.3pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Improper
  Validation of Array Index<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:15.3pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">17070<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE134<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Uncontrolled
  Format String<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">4128<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;height:15.3pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.3pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE15<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:15.3pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">External Control
  of System or Configuration Setting<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:15.3pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">1979<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:5;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE190<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Integer Overflow<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">27820<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:6;height:7.25pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.25pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE191<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.25pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Integer
  Underflow<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.25pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">22256<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:7;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE197<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Numeric
  Truncation Error<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">5409<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:8;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE23<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Relative Path
  Traversal<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">1979<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:9;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE259<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Hard Coded
  Password<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">528<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:10;height:15.3pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.3pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE319<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:15.3pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Cleartext
  Transmission of Sensitive Information<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:15.3pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">1942<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:11;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE369<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Divide by Zero<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">11752<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:12;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE36<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Absolute Path
  Traversal<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">1979<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:13;height:7.25pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.25pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE398<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.25pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Poor Code
  Quality<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.25pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">515<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:14;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE400<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Resource
  Exhaustion<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">9256<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:15;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE470<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Unsafe
  Reflection<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">1979<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:16;height:10.85pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:10.85pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE476<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:10.85pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">NULL Pointer
  Dereference<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:10.85pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">1185<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:17;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE506<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Embedded
  Malicious Code<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">259<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:18;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE563<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Unused Variable<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">934<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:19;height:7.25pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.25pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE601<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.25pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Open Redirect<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.25pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">1451<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:20;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE606<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Unchecked Loop
  Condition<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">2814<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:21;height:10.35pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:10.35pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE643<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:10.35pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Improper
  Neutralization of Data within XPath Expressions<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:10.35pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">879<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:22;height:15.3pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.3pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE690<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:15.3pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Unchecked Return
  Value to NULL Pointer Dereference<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:15.3pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">2000<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:23;height:15.3pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:15.3pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE789<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:15.3pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Uncontrolled
  Memory Allocation<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:15.3pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">7057<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:24;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE78<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">OS Command
  Injection<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">1979<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:25;height:7.25pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.25pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE80<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.25pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">Basic XSS<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.25pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">2902<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:26;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE81<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">XSS Error
  Message<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">1451<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:27;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE83<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">XSS Attribute<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">1451<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:28;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE89<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">SQL Injection<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">14070<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:29;height:7.65pt">
  <td width="61" style="width:45.45pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">CWE90<o:p></o:p></span></p>
  </td>
  <td width="291" style="width:218.1pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">LDAP Injection<o:p></o:p></span></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.65pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">639<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:30;mso-yfti-lastrow:yes;height:7.95pt">
  <td width="351" colspan="2" style="width:263.55pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:7.95pt">
  <p class="MsoNormal" align="right" style="text-align:right"><b style="mso-bidi-font-weight:
  normal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:110%;
  font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">total<o:p></o:p></span></b></p>
  </td>
  <td width="158" style="width:118.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:7.95pt">
  <p class="MsoNormal"><span lang="IT" style="mso-bidi-font-size:10.0pt;line-height:
  110%;font-family:&quot;Calibri&quot;,sans-serif;mso-fareast-font-family:&quot;Times New Roman&quot;;
  mso-bidi-font-family:&quot;Times New Roman&quot;;mso-ansi-language:IT">156105<o:p></o:p></span></p>
  </td>
 </tr>
</tbody></table>


# Run the code
To run the code, simply run "python MPDA.py train folder threshold net"
If you set the threshold to 100, the model will train and detect 29 vulnerabilities
Net, we provide four types of neural networks: lstm, gru, bilstm, and bigru
If you want to make modifications, please make them in the model.py file
data_augmentation.py contains our data augmentation algorithm