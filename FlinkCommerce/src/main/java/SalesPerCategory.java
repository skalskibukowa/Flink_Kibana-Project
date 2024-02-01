import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.sql.Date;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class SalesPerCategory {
    private Date transactionDate;
    private String category;
    private double totalSales;
}
