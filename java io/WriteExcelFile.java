import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileOutputStream;
import java.io.IOException;

public class WriteExcelFile {
    public static void main(String[] args) {
        String filePath = "path/to/your/file.xlsx"; // Update this with your file path

        // Create a new workbook
        try (Workbook workbook = new XSSFWorkbook()) {
            // Create a new sheet
            Sheet sheet = workbook.createSheet("Sheet1");

            // Create a row and put some cells in it. Rows are 0-based.
            Row row = sheet.createRow(0);

            // Create cells and set values
            Cell cell1 = row.createCell(0);
            cell1.setCellValue("Name");

            Cell cell2 = row.createCell(1);
            cell2.setCellValue("Age");

            Cell cell3 = row.createCell(2);
            cell3.setCellValue("Active");

            // Create another row and set more values
            Row row2 = sheet.createRow(1);

            Cell cell4 = row2.createCell(0);
            cell4.setCellValue("John");

            Cell cell5 = row2.createCell(1);
            cell5.setCellValue(30);

            Cell cell6 = row2.createCell(2);
            cell6.setCellValue(true);

            // Write the output to a file
            try (FileOutputStream fileOut = new FileOutputStream(filePath)) {
                workbook.write(fileOut);
            }

            System.out.println("Excel file written successfully!");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
