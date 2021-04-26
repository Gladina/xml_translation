import xml.etree.ElementTree as ET
from xml.etree import ElementTree
import pandas
import json
import xmltodict
import pandas
    
Hello = "value"

while True:
  try:
    print("\n")
    print("-------------------------- BEGIN --------------------------")
    print("Which language do you want to translate into: ")
    print("-----------------------------------------------------------")
    print("\n")
    lang = input ("Enter 'EN/English' for English, 'JP/Japanese' for Japanese: ") 
    if lang.lower() == "en" or lang.lower() == 'jp' or lang.lower() == "english" or lang.lower() == 'japanese':
        trans_lang = lang.upper()
        print("--------------------- GOOD TO GO --------------------------")
        print("Hurrah!, Input '"+trans_lang+"' recieved for Translation")
        print("-----------------------------------------------------------")
        print("\n")
        break
    else:
        print("-------------------------- ERROR --------------------------")
        print("Sorry, '"+lang.upper()+"' is not supported. Only 'EN/English', 'JP/Japanese' is supported.")
        print("-----------------------------------------------------------")
        print("\n")
  except KeyboardInterrupt:
    exit()

xml_english_source_1 = """<dashboard>
    <label>Host</label>
    <row>
        <panel>
            <single>
                <title>Host</title>
                <search>
                    <query>index="_internal" | top host</query>
                    <earliest>-24h@h</earliest>
                    <latest>now</latest>
                    <sampleRatio>1</sampleRatio>
                </search>
                <option name="colorBy">value</option>
                <option name="colorMode">none</option>
                <option name="drilldown">none</option>
                <option name="height">250</option>
                <option name="numberPrecision">0</option>
                <option name="rangeColors">["0x53a051", "0x0877a6", "0xf8be34", "0xf1813f",0xdc4e41]</option>
                <option name="rangeValues">[0,30,70,100]</option>
                <option name="showSparkline">1</option>
                <option name="showTrendIndicator">1</option>
                <option name="trellis.enabled">0</option>
                <option name="trellis.scales.shared">1</option>
                <option name="trellis.size">medium</option>
                <option name="trendColorInterpretation">standard</option>
                <option name="trendDisplayMode">absolute</option>
                <option name="unitPosition">after</option>
                <option name="useColors">0</option>
                <option name="useThousandSeparators">1</option>
            </single>
        </panel>
        <panel>
            <chart>
                <title>Host Timechart</title>
                <search>
                    <query>index="_internal" | timechart count by host</query>
                    <earliest>-24h@h</earliest>
                    <latest>now</latest>
                    <sampleRatio>1</sampleRatio>
                </search>
                <option name="charting.axisLabelsX.majorLabelStyle.overflowMode">ellipsisNone</option>
                <option name="charting.axisLabelsX.majorLabelStyle.rotation">0</option>
                <option name="charting.axisTitleX.visibility">visible</option>
                <option name="charting.axisTitleY.visibility">visible</option>
                <option name="charting.axisTitleY2.visibility">visible</option>
                <option name="charting.axisX.abbreviation">none</option>
                <option name="charting.axisX.scale">linear</option>
                <option name="charting.axisY.abbreviation">none</option>
                <option name="charting.axisY.scale">linear</option>
                <option name="charting.axisY2.abbreviation">none</option>
                <option name="charting.axisY2.enabled">0</option>
                <option name="charting.axisY2.scale">inherit</option>
                <option name="charting.chart">line</option>
                <option name="charting.chart.bubbleMaximumSize">50</option>
                <option name="charting.chart.bubbleMinimumSize">10</option>
                <option name="charting.chart.bubbleSizeBy">area</option>
                <option name="charting.chart.nullValueMode">gaps</option>
                <option name="charting.chart.showDataLabels">none</option>
                <option name="charting.chart.sliceCollapsingThreshold">0.01</option>
                <option name="charting.chart.stackMode">default</option>
                <option name="charting.chart.style">shiny</option>
                <option name="charting.drilldown">none</option>
                <option name="charting.layout.splitSeries">0</option>
                <option name="charting.layout.splitSeries.allowIndependentYRanges">0</option>
                <option name="charting.legend.labelStyle.overflowMode">ellipsisMiddle</option>
                <option name="charting.legend.mode">standard</option>
                <option name="charting.legend.placement">right</option>
                <option name="charting.lineWidth">2</option>
                <option name="trellis.enabled">0</option>
                <option name="trellis.scales.shared">1</option>
                <option name="trellis.size">medium</option>
            </chart>
        </panel>
    </row>
</dashboard>
"""

xml_japanese_source_1 = """<dashboard>
    <label>ホスト</label>
    <row>
        <panel>
            <single>
                <title>ホスト</title>
                <search>
                    <query>index="_internal" | top host</query>
                    <earliest>-24h@h</earliest>
                    <latest>now</latest>
                    <sampleRatio>1</sampleRatio>
                </search>
                <option name="colorBy">value</option>
                <option name="colorMode">none</option>
                <option name="drilldown">none</option>
                <option name="height">250</option>
                <option name="numberPrecision">0</option>
                <option name="rangeColors">["0x53a051", "0x0877a6", "0xf8be34", "0xf1813f",0xdc4e41]</option>
                <option name="rangeValues">[0,30,70,100]</option>
                <option name="showSparkline">1</option>
                <option name="showTrendIndicator">1</option>
                <option name="trellis.enabled">0</option>
                <option name="trellis.scales.shared">1</option>
                <option name="trellis.size">medium</option>
                <option name="trendColorInterpretation">standard</option>
                <option name="trendDisplayMode">absolute</option>
                <option name="unitPosition">after</option>
                <option name="useColors">0</option>
                <option name="useThousandSeparators">1</option>
            </single>
        </panel>
        <panel>
            <chart>
                <title>ホストタイムチャート</title>
                <search>
                    <query>index="_internal" | timechart count by host</query>
                    <earliest>-24h@h</earliest>
                    <latest>now</latest>
                    <sampleRatio>1</sampleRatio>
                </search>
                <option name="charting.axisLabelsX.majorLabelStyle.overflowMode">ellipsisNone</option>
                <option name="charting.axisLabelsX.majorLabelStyle.rotation">0</option>
                <option name="charting.axisTitleX.visibility">visible</option>
                <option name="charting.axisTitleY.visibility">visible</option>
                <option name="charting.axisTitleY2.visibility">visible</option>
                <option name="charting.axisX.abbreviation">none</option>
                <option name="charting.axisX.scale">linear</option>
                <option name="charting.axisY.abbreviation">none</option>
                <option name="charting.axisY.scale">linear</option>
                <option name="charting.axisY2.abbreviation">none</option>
                <option name="charting.axisY2.enabled">0</option>
                <option name="charting.axisY2.scale">inherit</option>
                <option name="charting.chart">line</option>
                <option name="charting.chart.bubbleMaximumSize">50</option>
                <option name="charting.chart.bubbleMinimumSize">10</option>
                <option name="charting.chart.bubbleSizeBy">area</option>
                <option name="charting.chart.nullValueMode">gaps</option>
                <option name="charting.chart.showDataLabels">none</option>
                <option name="charting.chart.sliceCollapsingThreshold">0.01</option>
                <option name="charting.chart.stackMode">default</option>
                <option name="charting.chart.style">shiny</option>
                <option name="charting.drilldown">none</option>
                <option name="charting.layout.splitSeries">0</option>
                <option name="charting.layout.splitSeries.allowIndependentYRanges">0</option>
                <option name="charting.legend.labelStyle.overflowMode">ellipsisMiddle</option>
                <option name="charting.legend.mode">standard</option>
                <option name="charting.legend.placement">right</option>
                <option name="charting.lineWidth">2</option>
                <option name="trellis.enabled">0</option>
                <option name="trellis.scales.shared">1</option>
                <option name="trellis.size">medium</option>
            </chart>
        </panel>
    </row>
</dashboard>
"""

xml_english_source_2 = """<dashboard>
    <label>Sourcetype</label>
    <row>
        <panel>
            <chart>
                <title>Source Type by Area</title>
                <search>
                    <query>index="_internal" | top sourcetype</query>
                    <earliest>-24h@h</earliest>
                    <latest>now</latest>
                    <sampleRatio>1</sampleRatio>
                </search>
                <option name="charting.axisLabelsX.majorLabelStyle.overflowMode">ellipsisNone</option>
                <option name="charting.axisLabelsX.majorLabelStyle.rotation">0</option>
                <option name="charting.axisTitleX.visibility">visible</option>
                <option name="charting.axisTitleY.visibility">visible</option>
                <option name="charting.axisTitleY2.visibility">visible</option>
                <option name="charting.axisX.abbreviation">none</option>
                <option name="charting.axisX.scale">linear</option>
                <option name="charting.axisY.abbreviation">none</option>
                <option name="charting.axisY.scale">linear</option>
                <option name="charting.axisY2.abbreviation">none</option>
                <option name="charting.axisY2.enabled">0</option>
                <option name="charting.axisY2.scale">inherit</option>
                <option name="charting.chart">area</option>
                <option name="charting.chart.bubbleMaximumSize">50</option>
                <option name="charting.chart.bubbleMinimumSize">10</option>
                <option name="charting.chart.bubbleSizeBy">area</option>
                <option name="charting.chart.nullValueMode">gaps</option>
                <option name="charting.chart.showDataLabels">none</option>
                <option name="charting.chart.sliceCollapsingThreshold">0.01</option>
                <option name="charting.chart.stackMode">default</option>
                <option name="charting.chart.style">shiny</option>
                <option name="charting.drilldown">none</option>
                <option name="charting.layout.splitSeries">0</option>
                <option name="charting.layout.splitSeries.allowIndependentYRanges">0</option>
                <option name="charting.legend.labelStyle.overflowMode">ellipsisMiddle</option>
                <option name="charting.legend.mode">standard</option>
                <option name="charting.legend.placement">right</option>
                <option name="charting.lineWidth">2</option>
                <option name="trellis.enabled">0</option>
                <option name="trellis.scales.shared">1</option>
                <option name="trellis.size">medium</option>
            </chart>
        </panel>
        <panel>
            <table>
                <title>Top sourcetype</title>
                <search>
                    <query>index="_internal" | top name</query>
                    <earliest>-24h@h</earliest>
                    <latest>now</latest>
                </search>
                <option name="drilldown">none</option>
            </table>
        </panel>
    </row>
</dashboard>
"""

xml_japanese_source_2 = """<dashboard>
    <label>ソースの種類</label>
    <row>
        <panel>
            <chart>
                <title>エリア別ソースタイプ</title>
                <search>
                    <query>index="_internal" | top sourcetype</query>
                    <earliest>-24h@h</earliest>
                    <latest>now</latest>
                    <sampleRatio>1</sampleRatio>
                </search>
                <option name="charting.axisLabelsX.majorLabelStyle.overflowMode">ellipsisNone</option>
                <option name="charting.axisLabelsX.majorLabelStyle.rotation">0</option>
                <option name="charting.axisTitleX.visibility">visible</option>
                <option name="charting.axisTitleY.visibility">visible</option>
                <option name="charting.axisTitleY2.visibility">visible</option>
                <option name="charting.axisX.abbreviation">none</option>
                <option name="charting.axisX.scale">linear</option>
                <option name="charting.axisY.abbreviation">none</option>
                <option name="charting.axisY.scale">linear</option>
                <option name="charting.axisY2.abbreviation">none</option>
                <option name="charting.axisY2.enabled">0</option>
                <option name="charting.axisY2.scale">inherit</option>
                <option name="charting.chart">area</option>
                <option name="charting.chart.bubbleMaximumSize">50</option>
                <option name="charting.chart.bubbleMinimumSize">10</option>
                <option name="charting.chart.bubbleSizeBy">area</option>
                <option name="charting.chart.nullValueMode">gaps</option>
                <option name="charting.chart.showDataLabels">none</option>
                <option name="charting.chart.sliceCollapsingThreshold">0.01</option>
                <option name="charting.chart.stackMode">default</option>
                <option name="charting.chart.style">shiny</option>
                <option name="charting.drilldown">none</option>
                <option name="charting.layout.splitSeries">0</option>
                <option name="charting.layout.splitSeries.allowIndependentYRanges">0</option>
                <option name="charting.legend.labelStyle.overflowMode">ellipsisMiddle</option>
                <option name="charting.legend.mode">standard</option>
                <option name="charting.legend.placement">right</option>
                <option name="charting.lineWidth">2</option>
                <option name="trellis.enabled">0</option>
                <option name="trellis.scales.shared">1</option>
                <option name="trellis.size">medium</option>
            </chart>
        </panel>
        <panel>
            <table>
                <title>トップソースタイプ</title>
                <search>
                    <query>index="_internal" | top name</query>
                    <earliest>-24h@h</earliest>
                    <latest>now</latest>
                </search>
                <option name="drilldown">none</option>
            </table>
        </panel>
    </row>
</dashboard>
"""

#Read excel lookup.xlsx and form translation lists []
excel_data_df = pandas.read_excel('lookup.xlsx', sheet_name='Sheet1')
lkup_json = excel_data_df.to_json(orient='records')
result_en_as_dict = []
result_jp_as_dict = []
lookup = json.loads(lkup_json)
for data in lookup:
    ##print(data["English"])
    ##print(data["Japanese"])
    en_dict = {
        'key': data["Japanese"],
        'value': data["English"]
    }
    #Create / Append EN LIST
    result_en_as_dict.append(en_dict)

    jp_dict = {
        'key': data["English"],
        'value': data["Japanese"]
    }
    #Create / Append JP LIST
    result_jp_as_dict.append(jp_dict)

#XML_SOURCE_1 Based on user translation lang assign xml_tree to process translation of nodes that exists in English, Japanese in the excel fiedls
if lang.lower() == "en" or lang.lower() == 'jp' or lang.lower() == "english" or lang.lower() == 'japanese':
    source_file_name_one = "source_XML_1_"+trans_lang+".xml"
    if lang.lower() == "en" or lang.lower() == "english":
        source_xml_list = result_en_as_dict
        xml_1 = xml_japanese_source_1
        print("JAPANESE_XML_Source_1 List has been picked for translation.")
        print("\n")
    if lang.lower() == "jp" or lang.lower() == "japanese":
        source_xml_list = result_jp_as_dict  
        xml_1 = xml_english_source_1
        print("ENGLISH_XML_Source_1 List has been picked for translation.")
        print("\n")
tree = ET.fromstring(xml_1)

#traverse through xml data to find nodes whichever matches against the values / fields in the lookup.xlsx and apply translation
for tag in tree.iter():
    #print(tag)
    for jp in source_xml_list:
        if tag.text == jp['key']:
            for jp in source_xml_list:
                if jp['key'] == tag.text:
                    #print("exists key")
                    tag.text = jp['value']
        else:
            pass
            #print("NOT exists key")

#create new source xml 1 after translation
xmlstring = ET.tostring(tree).decode("utf-8", errors="ignore")
with open(source_file_name_one, "w") as f:
    f.write(xmlstring)
    print("------------------------------------ TRANSLATED SOURCE 1 -----------------------------------------------")
    print("Done. File by name "+source_file_name_one+" has been created in the application root directory.")
    print("\n")
    print("\n")

#XML_SOURCE_1 Based on user translation lang assign xml_tree to process translation of nodes that exists in English, Japanese in the excel fiedls
if lang.lower() == "en" or lang.lower() == 'jp' or lang.lower() == "english" or lang.lower() == 'japanese':
    source_file_name_two = "source_XML_2_"+trans_lang+".xml"
    if lang.lower() == "en" or lang.lower() == "english":
        source_xml_list = result_en_as_dict
        xml_2 = xml_japanese_source_2
        print("JAPANESE_XML_Source_2 List has been picked for translation.")
        print("\n")
    if lang.lower() == "jp" or lang.lower() == "japanese":
        source_xml_list = result_jp_as_dict  
        xml_2 = xml_english_source_2
        print("ENGLISH_XML_Source_2 List has been picked for translation.")
        print("\n")
tree = ET.fromstring(xml_2)

#traverse through xml data to find nodes whichever matches against the values / fields in the lookup.xlsx and apply translation
for tag in tree.iter():
    #print(tag)
    for jp in source_xml_list:
        if tag.text == jp['key']:
            for jp in source_xml_list:
                if jp['key'] == tag.text:
                    #print("exists key")
                    tag.text = jp['value']
        else:
            pass
            #print("NOT exists key")

#create new source xml 2 after translation
xmlstring = ET.tostring(tree).decode("utf-8", errors="ignore")
with open(source_file_name_two, "w") as f:
    f.write(xmlstring)
    print("------------------------------------ TRANSLATED SOURCE 2 -----------------------------------------------")
    print("Done. File by name "+source_file_name_two+" has been created in the application root directory.")
