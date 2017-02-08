import java.io.File;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Element;

public class CorpusGenerator {
	// http://www.mkyong.com/java/how-to-create-xml-file-in-java-dom/
		// https://github.com/greenbird/xml-formatter-core

		// DocumentBuilder
		private DocumentBuilderFactory docFactory;
		private DocumentBuilder docBuilder;

		// Dokument
		private Document doc;
		private Element rootElement;

		public CorpusGenerator() {

			docFactory = DocumentBuilderFactory.newInstance();
			try {
				docBuilder = docFactory.newDocumentBuilder();
			} catch (ParserConfigurationException e) {
				// TODO Auto-generated catch block
				if (Configurations.showExceptions) {
					e.printStackTrace();
				}
			}
			baueKorpusdateiStruktur();
		}

		private void baueKorpusdateiStruktur() {
			// root elements
			doc = docBuilder.newDocument();

			rootElement = doc.createElement("corpus");
			doc.appendChild(rootElement);

		}
		
		public void createCorpusfileBody(int songId, String songTitle, String songText, String releaseDate, String songAlbum, String songAuthor, String filePath){
			
			Element song = doc.createElement("song");
			rootElement.appendChild(song);
			
			Element id = doc.createElement("id");
			id.appendChild(doc.createTextNode(Integer.toString(songId)));
			song.appendChild(id);
			
			Element title = doc.createElement("title");
			title.appendChild(doc.createTextNode(songTitle));
			song.appendChild(title);
			
			Element date = doc.createElement("date");
			date.appendChild(doc.createTextNode(releaseDate));
			song.appendChild(date);
			
			Element album = doc.createElement("album");
			album.appendChild(doc.createTextNode(songAlbum));
			song.appendChild(album);
			
			Element author = doc.createElement("author");
			author.appendChild(doc.createTextNode(songAuthor));
			song.appendChild(author);
			
			Element text = doc.createElement("text");
			text.appendChild(doc.createTextNode(songText));
			song.appendChild(text);
			
			if(songText.equals("")){
				System.out.println("###FEHLERHAFTE DATEI: " + filePath);
			}
			
		}

		public void generateCorpusFile(String dateiname) {
			System.out.println("_____________________Erstelle Korpusdatei " + dateiname + ".xml");
			try {
				// write the content into xml file
				TransformerFactory transformerFactory = TransformerFactory
						.newInstance();
				Transformer transformer = transformerFactory.newTransformer();
				transformer.setOutputProperty(OutputKeys.METHOD, "xml");
				transformer.setOutputProperty(OutputKeys.INDENT, "yes");
				/*
				 * transformer.setOutputProperty(
				 * "http://xml.apache.org/xsltd;indent-amount", "4");
				 */
				DOMSource source = new DOMSource(doc);
				StreamResult result = new StreamResult(new File("./stringdata/"
						+ dateiname + ".xml"));

				transformer.setOutputProperty(
						"{http://xml.apache.org/xslt}indent-amount", "2");
				transformer.transform(source, result);

				System.out.println("_____________________Neue Korpusdatei " + dateiname
						+ ".xml erfolgreich gespeichert!");

			} catch (TransformerException tfe) {
				if (Configurations.showExceptions) {
					tfe.printStackTrace();
				}
			}
		}
}
